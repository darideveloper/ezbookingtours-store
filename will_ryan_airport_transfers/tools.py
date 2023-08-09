from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

def send_sucess_mail (id:int, first_name:str, last_name:str, 
                      price:float, details:list, email:str):
    """ Send sucess email to buyer

    Args:
        id (int): sale id
        first_name (str): buyer first name
        last_name (str): buyer last name
        price (float): sale price
        details (list): sale full details
        email (str): buyer email
    """
    
    # Get template path
    current_folder = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_folder, "templates", "will_ryan_airport_transfers", 'mail.html')
    
    # Get html and plain message
    context = {
        "id": id, 
        "first_name": first_name, 
        "last_name": last_name, 
        "price": price, 
        "details": details
    }
    html_message = render_to_string(template_path, context)
    plain_message = strip_tags(html_message)
    
    # Create message, attach html message and submit
    message = EmailMultiAlternatives("Voucher Will Ryan Airport Transfers",
                                    plain_message,
                                    settings.EMAIL_HOST_USER,
                                    [email])
    message.attach_alternative(html_message, "text/html")
    message.send()