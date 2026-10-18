from django.core import mail
from django.test import TestCase, override_settings


@override_settings(EMAIL_CLIENT="admin@example.com")
class TestEmailEndpointTests(TestCase):
    """Regression tests for the /test-email/ SMTP diagnostic endpoint."""

    def test_test_email_sets_reply_to(self):
        response = self.client.get(
            "/test-email/", {"email": "guest@example.com", "send": "true"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        self.assertEqual(len(mail.outbox), 1)

        message = mail.outbox[0]
        self.assertEqual(message.to, ["guest@example.com"])
        self.assertEqual(message.reply_to, ["admin@example.com"])

    @override_settings(EMAIL_CLIENT="")
    def test_test_email_without_admin_inbox_omits_reply_to(self):
        response = self.client.get(
            "/test-email/", {"email": "guest@example.com", "send": "true"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].reply_to, [])
