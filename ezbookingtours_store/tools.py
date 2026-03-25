from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
import os


def parse_dt(value, formats):
    """Parse a date or time string using a list of possible formats.

    Args:
        value (str): The string to parse.
        formats (list): A list of format strings to try.

    Returns:
        datetime|date|time|None: The parsed object or None if no format matches.
    """
    if not value:
        return None
        
    for fmt in formats:
        try:
            dt = datetime.strptime(value, fmt)
            if "%H:%M" in fmt:
                return dt.time()
            if "%Y-%m-%d" in fmt:
                return dt.date()
            return dt
        except ValueError:
            continue
    return None


def send_sucess_mail(
    subjects: list,
    template_path: str,
    id: int,
    first_name: str,
    last_name: str,
    price: float,
    details: list,
    from_email: str = None,
    host: str = None,
    email: str = None,
):
    """Send sucess email to buyer

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

    print(f"[DEBUG] TOOLS - Starting send_sucess_mail for ID: {id}, To: {email}")
    # Use defaults from settings if not provided
    if not from_email:
        from_email = settings.EMAIL_HOST_USER
    if not host:
        host = settings.EMAIL_HOST

    # Get html and plain message
    context = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "price": price,
        "details": details,
    }
    
    try:
        html_message = render_to_string(template_path, context)
        plain_message = strip_tags(html_message)
        print(f"[DEBUG] TOOLS - Email rendered successfully using template: {template_path}")
    except Exception as e:
        print(f"[DEBUG] TOOLS - Error rendering email template: {str(e)}")
        raise

    # Create message, attach html message and submit
    try:
        connection = get_connection(
            host=host,
            port=settings.EMAIL_PORT,
            username=from_email,
            password=settings.EMAIL_HOST_PASSWORD,
        )
        print(f"[DEBUG] TOOLS - SMTP Connection established with: {host}:{settings.EMAIL_PORT}")
    except Exception as e:
        print(f"[DEBUG] TOOLS - Error connecting to SMTP: {str(e)}")
        raise

    # Send email to client
    try:
        message = EmailMultiAlternatives(
            subjects[0], plain_message, from_email, [email], connection=connection
        )
        message.attach_alternative(html_message, "text/html")
        message.send()
        print(f"[DEBUG] TOOLS - Client email sent successfully to: {email}")
    except Exception as e:
        print(f"[DEBUG] TOOLS - Error sending client email: {str(e)}")
        raise

    # Send email to admin
    try:
        admin_email = settings.EMAIL_CLIENT
        message = EmailMultiAlternatives(
            subjects[1],
            plain_message,
            from_email,
            [admin_email],
            connection=connection,
        )
        message.attach_alternative(html_message, "text/html")
        message.send()
        print(f"[DEBUG] TOOLS - Admin email sent successfully to: {admin_email}")
    except Exception as e:
        print(f"[DEBUG] TOOLS - Error sending admin email: {str(e)}")
        raise
