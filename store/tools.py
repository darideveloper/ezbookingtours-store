from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

def send_sucess_mail (context):
    
    # Get template path
    current_folder = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_folder, "templates", "store", 'success.html')
    
    # Update context
    copy_context = context.copy()
    copy_context["is_email"] = True
    
    # Get html and plain message
    html_message = render_to_string(template_path, copy_context)
    plain_message = strip_tags(html_message)
    
    # Create message, attach html message and submit
    message = EmailMultiAlternatives("Nuevo proceso de compra iniciado",
                                    plain_message,
                                    settings.EMAIL_HOST_USER,
                                    [settings.EMAIL_CLIENT])
    message.attach_alternative(html_message, "text/html")
    message.send()