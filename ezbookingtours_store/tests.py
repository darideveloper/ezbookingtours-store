from unittest.mock import patch

from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.test import SimpleTestCase, override_settings

from ezbookingtours_store.email_backend import ReplyToEmailBackend


@override_settings(EMAIL_REPLY_TO="admin@example.com")
class ReplyToEmailBackendTests(SimpleTestCase):
    """The backend guarantees a Reply-To header without overwriting one."""

    def _send(self, message):
        backend = ReplyToEmailBackend()
        with patch.object(EmailBackend, "send_messages", return_value=1):
            return backend.send_messages([message])

    def test_injects_reply_to_when_missing(self):
        message = EmailMessage("Subject", "Body", "from@example.com", ["client@example.com"])

        self._send(message)

        self.assertEqual(message.reply_to, ["admin@example.com"])

    def test_does_not_overwrite_existing_reply_to(self):
        message = EmailMessage(
            "Subject",
            "Body",
            "from@example.com",
            ["client@example.com"],
            reply_to=["existing@example.com"],
        )

        self._send(message)

        self.assertEqual(message.reply_to, ["existing@example.com"])

    @override_settings(EMAIL_REPLY_TO="")
    def test_skips_injection_when_unset(self):
        message = EmailMessage("Subject", "Body", "from@example.com", ["client@example.com"])

        self._send(message)

        self.assertEqual(message.reply_to, [])
