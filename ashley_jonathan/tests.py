import json
from unittest.mock import patch, MagicMock
from django.test import TestCase, Client, override_settings
from django.core import mail
from django.contrib import admin
from django.contrib.auth.models import User
from ashley_jonathan import models


@override_settings(STATICFILES_STORAGE="django.contrib.staticfiles.storage.StaticFilesStorage")
class AshleyJonathanTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.arrival_payload = {
            "products": {
                "Airport - Hotel Transfer": {
                    "price": 0,
                    "description": {
                        "name": "Jane",
                        "last_name": "Doe",
                        "email": "jane@example.com",
                        "passengers": 4,
                        "transport_vehicle": "van",
                        "arriving_airline": "Delta",
                        "arriving_flight_number": "DL123",
                        "arriving_date": "2026-11-01",
                        "arriving_time": "14:30",
                        "arriving_hotel": "Maroma, A Belmond Hotel",
                    },
                }
            }
        }
        self.departure_payload = {
            "products": {
                "Hotel - Airport Transfer": {
                    "price": 10,
                    "description": {
                        "name": "Jane",
                        "last_name": "Doe",
                        "email": "jane@example.com",
                        "passengers": 4,
                        "transport_vehicle": "van",
                        "departing_airline": "Delta",
                        "departing_flight_number": "DL456",
                        "departing_date": "2026-11-05",
                        "departing_time": "11:00",
                        "departing_hotel": "Maroma, A Belmond Hotel",
                    },
                }
            }
        }
        self.round_trip_payload = {
            "products": {
                "Round Trip Transfer": {
                    "price": 10,
                    "description": {
                        "name": "Jane",
                        "last_name": "Doe",
                        "email": "jane@example.com",
                        "passengers": 4,
                        "transport_vehicle": "van",
                        "arriving_airline": "Delta",
                        "arriving_flight_number": "DL123",
                        "departing_airline": "Delta",
                        "departing_flight_number": "DL456",
                    },
                }
            }
        }

    def test_free_arrival_booking_success(self):
        """Arrival service must be 100% free, saved immediately as done, and email sent."""
        response = self.client.post(
            "/ashley-jonathan/sale/",
            data=json.dumps(self.arrival_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data.get("free"))
        self.assertIn("?done=true", data.get("stripe_url", ""))

        # Verify database record
        sale = models.Sale.objects.filter(email="jane@example.com").first()
        self.assertIsNotNone(sale)
        self.assertTrue(sale.sale_done)
        self.assertEqual(sale.price, 0)
        self.assertEqual(sale.transport_vehicule, "van")
        self.assertIn("Delta", sale.arriving)

        # Verify confirmation emails sent
        self.assertEqual(len(mail.outbox), 2)
        subjects = [m.subject for m in mail.outbox]
        self.assertTrue(any("Ashley & Jonathan Wedding" in s for s in subjects))

    def test_arrival_with_non_zero_price_still_treated_as_free(self):
        """Any arrival transfer must be free regardless of price payload."""
        payload = json.loads(json.dumps(self.arrival_payload))
        payload["products"]["Airport - Hotel Transfer"]["price"] = 99
        response = self.client.post(
            "/ashley-jonathan/sale/",
            data=json.dumps(payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        sale = models.Sale.objects.filter(email="jane@example.com").first()
        self.assertIsNotNone(sale)
        self.assertTrue(sale.sale_done)
        self.assertEqual(sale.price, 0)

    @patch("requests.post")
    def test_paid_departure_booking_creates_stripe_session(self, mock_post):
        """Departure transfer must not be free and must call Stripe API."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "stripe_url": "https://checkout.stripe.com/pay/cs_test_departure"
        }
        mock_post.return_value = mock_response

        response = self.client.post(
            "/ashley-jonathan/sale/",
            data=json.dumps(self.departure_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get("stripe_url"), "https://checkout.stripe.com/pay/cs_test_departure")

        # Verify sale is pending (not done)
        sale = models.Sale.objects.filter(email="jane@example.com").first()
        self.assertIsNotNone(sale)
        self.assertFalse(sale.sale_done)
        self.assertEqual(sale.price, 10)
        self.assertEqual(len(mail.outbox), 0)

    @patch("requests.post")
    def test_paid_round_trip_booking_creates_stripe_session(self, mock_post):
        """Round trip transfer must be charged at the departure price and invoke Stripe."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "stripe_url": "https://checkout.stripe.com/pay/cs_test_roundtrip"
        }
        mock_post.return_value = mock_response

        response = self.client.post(
            "/ashley-jonathan/sale/",
            data=json.dumps(self.round_trip_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get("stripe_url"), "https://checkout.stripe.com/pay/cs_test_roundtrip")

        sale = models.Sale.objects.filter(email="jane@example.com").first()
        self.assertIsNotNone(sale)
        self.assertFalse(sale.sale_done)
        self.assertEqual(sale.price, 10)

    def test_sale_done_view_success(self):
        """SaleDoneView completes pending sale, sends email, and redirects."""
        sale = models.Sale.objects.create(
            transport_type="Hotel - Airport Transfer",
            name="John",
            last_name="Smith",
            email="john@example.com",
            passengers=2,
            price=10,
            departing="airline: Delta |\n flight_number: DL789 |\n",
            transport_vehicule="sprinter",
            sale_done=False,
        )

        response = self.client.get(f"/ashley-jonathan/sale/{sale.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("?done=true", response.url)

        sale.refresh_from_db()
        self.assertTrue(sale.sale_done)
        self.assertEqual(len(mail.outbox), 2)

    def test_sale_done_view_preview(self):
        """SaleDoneView in preview returns rendered html without emailing."""
        sale = models.Sale.objects.create(
            transport_type="Airport - Hotel Transfer",
            name="Preview",
            last_name="User",
            email="preview@example.com",
            passengers=1,
            price=0,
            sale_done=False,
        )
        response = self.client.get(f"/ashley-jonathan/sale/{sale.id}/?preview=true")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])
        self.assertEqual(len(mail.outbox), 0)

    def test_sale_done_view_not_found(self):
        """Non-existent sale id returns 404."""
        response = self.client.get("/ashley-jonathan/sale/999999/")
        self.assertEqual(response.status_code, 404)

    def test_admin_registration(self):
        """Sale model must be properly registered in admin."""
        self.assertIn(models.Sale, admin.site._registry)
        user = User.objects.create_superuser("admin_user", "admin@example.com", "password")
        self.client.force_login(user)
        response = self.client.get("/admin/ashley_jonathan/sale/")
        self.assertEqual(response.status_code, 200)
