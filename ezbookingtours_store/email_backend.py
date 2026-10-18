from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend


class ReplyToEmailBackend(EmailBackend):
    """SMTP backend that guarantees a Reply-To header on outgoing mail.

    Safety net for send sites that do not pass ``reply_to`` explicitly:
    any message without one is pointed at ``EMAIL_REPLY_TO`` (which reuses
    ``EMAIL_CLIENT``). Messages that already define ``reply_to`` are left
    untouched. When ``EMAIL_REPLY_TO`` is unset/empty, nothing is injected,
    so local runs without email configuration keep working.
    """

    def send_messages(self, email_messages):
        reply_to = settings.EMAIL_REPLY_TO
        if reply_to:
            for message in email_messages:
                if not message.reply_to:
                    message.reply_to = [reply_to]
        return super().send_messages(email_messages)
