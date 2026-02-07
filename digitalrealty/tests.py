from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
import json
from digitalrealty.models import Sale


class SaleViewTestCase(TestCase):
    """Test cases for SaleView"""

    def setUp(self):
        self.client = Client()
        self.sale_url = "/digitalrealty/sale/"

    @patch("digitalrealty.views.requests.post")
    def test_create_sale_success(self, mock_post):
        """Test POST request creates sale and returns stripe response"""
        # Mock stripe API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"url": "https://checkout.stripe.com/test123"}
        mock_post.return_value = mock_response

        # Request data
        data = {
            "products": {
                "round_trip": {
                    "price": 150,
                    "description": {
                        "name": "John",
                        "last_name": "Doe",
                        "email": "john@example.com",
                        "passengers": 2,
                        "transport_vehicle": "SUV",
                        "arriving_date": "2024-01-15",
                        "arriving_flight": "AA123",
                        "departing_date": "2024-01-20",
                        "departing_flight": "AA456",
                    },
                }
            }
        }

        response = self.client.post(
            self.sale_url, json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("url", response.json())

        # Verify sale was created
        sale = Sale.objects.first()
        self.assertIsNotNone(sale)
        self.assertEqual(sale.name, "John")
        self.assertEqual(sale.last_name, "Doe")
        self.assertEqual(sale.email, "john@example.com")
        self.assertEqual(sale.price, 150)
        self.assertEqual(sale.passengers, 2)


class SaleDoneViewTestCase(TestCase):
    """Test cases for SaleDoneView"""

    def setUp(self):
        self.client = Client()
        # Create a test sale
        self.sale = Sale.objects.create(
            transport_type="round_trip",
            name="Jane",
            last_name="Smith",
            email="jane@example.com",
            passengers=3,
            price=200,
            arriving="date: 2024-01-15 |\nflight: AA123 |\n",
            departing="date: 2024-01-20 |\nflight: AA456 |\n",
            transport_vehicule="Van",
            sale_done=False,
        )

    def test_sale_not_found(self):
        """Test GET request for non-existent sale returns 404"""
        response = self.client.get("/digitalrealty/sale/99999/")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Venta no encontrada")

    @patch("digitalrealty.views.EmailMultiAlternatives")
    def test_sale_done_preview_mode(self, mock_email):
        """Test GET request in preview mode returns HTML without sending email"""
        response = self.client.get(f"/digitalrealty/sale/{self.sale.id}/?preview=true")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Jane", response.content)

        # Verify sale was marked as done
        self.sale.refresh_from_db()
        self.assertTrue(self.sale.sale_done)

        # Verify email was NOT sent (preview mode)
        mock_email.return_value.send.assert_not_called()

    @patch("digitalrealty.views.EmailMultiAlternatives")
    @patch("digitalrealty.views.DIGITALREALTY_PAGE", "https://test.com/digitalrealty")
    def test_sale_done_redirects(self, mock_email):
        """Test GET request marks sale as done and redirects"""
        mock_email.return_value.send = MagicMock()

        response = self.client.get(f"/digitalrealty/sale/{self.sale.id}/")

        # Should redirect
        self.assertEqual(response.status_code, 302)

        # Verify sale was marked as done
        self.sale.refresh_from_db()
        self.assertTrue(self.sale.sale_done)


class SaleModelTestCase(TestCase):
    """Test cases for Sale model"""

    def test_sale_str_representation(self):
        """Test Sale __str__ method"""
        sale = Sale.objects.create(
            transport_type="one_way",
            name="Test",
            last_name="User",
            email="test@example.com",
        )

        self.assertEqual(str(sale), "Test User - one_way")

    def test_sale_default_values(self):
        """Test Sale default field values"""
        sale = Sale.objects.create(
            name="Test",
            last_name="User",
        )

        self.assertEqual(sale.passengers, 1)
        self.assertEqual(sale.price, 0)
        self.assertEqual(sale.sale_done, False)
        self.assertEqual(sale.transport_type, "")
