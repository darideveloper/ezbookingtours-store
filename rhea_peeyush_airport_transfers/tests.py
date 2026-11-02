from unittest.mock import patch

from django.test import TestCase

from rhea_peeyush_airport_transfers import models
from rhea_peeyush_airport_transfers.views import HOST

RETURN_URL = "https://cancunconciergedmc.com/rhea-peeyush-airport-transfers"


class SuccessViewTests(TestCase):
    def setUp(self):
        self.sale = models.Sale.objects.create(
            name="Jane", last_name="Doe", email="jane@example.com"
        )

    def test_unknown_url_returns_404(self):
        """The custom 404 handler must answer with a real 404 status."""
        self.assertEqual(self.client.get("/this-url-does-not-exist/").status_code, 404)

    def test_missing_trailing_slash_redirects(self):
        """Django APPEND_SLASH repairs the slash-less success URL."""
        response = self.client.get(f"/rhea-peeyush/success/{self.sale.id}")

        self.assertEqual(response.status_code, 301)
        self.assertTrue(
            response["Location"].endswith(f"/rhea-peeyush/success/{self.sale.id}/")
        )

    @patch("rhea_peeyush_airport_transfers.views.tools.send_sucess_mail")
    def test_buy_returns_slashed_success_url(self, _mail):
        """The redirect sent to the widget points at a real URL."""
        response = self.client.post(
            "/rhea-peeyush/buy/",
            data={
                "name": "Jane",
                "last-name": "Doe",
                "price": 0,
                "vip-code": "",
                "from-host": f"{RETURN_URL}/",
                "phone": "123456789",
                "email": "jane@example.com",
                "stripe-data": {
                    "transfer": {"description": "date:2026-11-10,hotel:Hilton"}
                },
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        sale = models.Sale.objects.latest("id")
        self.assertEqual(
            response.json()["redirect"],
            f"{HOST}/rhea-peeyush/success/{sale.id}/?from={RETURN_URL}",
        )

    def test_success_marks_paid_and_redirects_back(self):
        """A valid success URL marks the sale as paid and returns to the client."""
        response = self.client.get(
            f"/rhea-peeyush/success/{self.sale.id}/?from={RETURN_URL}"
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], f"{RETURN_URL}/?thanks=true")
        self.sale.refresh_from_db()
        self.assertTrue(self.sale.is_paid)

    def test_success_without_from_returns_404_but_keeps_paid(self):
        """No return URL shows the 404 page without losing the payment."""
        response = self.client.get(f"/rhea-peeyush/success/{self.sale.id}/")

        self.assertEqual(response.status_code, 404)
        self.sale.refresh_from_db()
        self.assertTrue(self.sale.is_paid)

    def test_success_unknown_sale_returns_404(self):
        """An unknown id must not crash with a 500."""
        response = self.client.get(f"/rhea-peeyush/success/999999/?from={RETURN_URL}")

        self.assertEqual(response.status_code, 404)
