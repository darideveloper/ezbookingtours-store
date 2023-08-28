from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

def send_sucess_mail (subjects:list,template_path:str, id:int, 
                      first_name:str, last_name:str, 
                      price:float, details:list, 
                      from_email:str, host:str, email:str):
    """ Send sucess email to buyer

    Args:
        subjects (list): list of subjects (for client and admin)
        template_path (str): template path
        id (int): sale id
        first_name (str): buyer first name
        last_name (str): buyer last name
        price (float): sale price
        details (list): sale full details
        from_email (str): from email
        host (str): email host
        email (str): buyer email
    """
    
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
    connection = get_connection(
        host=host,
        port=settings.EMAIL_PORT,
        username=from_email,
        password=settings.EMAIL_HOST_PASSWORD,
    )
    
    # Send email to client
    message = EmailMultiAlternatives(subjects[0],
                                    plain_message,
                                    from_email,
                                    [email], 
                                    connection=connection)
    message.attach_alternative(html_message, "text/html")
    message.send()
    
    # Send email to admin
    message = EmailMultiAlternatives(subjects[1],
                                    plain_message,
                                    from_email,
                                    [settings.EMAIL_CLIENT], 
                                    connection=connection)
    message.attach_alternative(html_message, "text/html")
    message.send()