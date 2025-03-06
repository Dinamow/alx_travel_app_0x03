from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation_email(user_email, booking_details):
    subject = "Booking Confirmation"
    message = f"Dear customer, your booking has been confirmed.\n\nDetails:\n{booking_details}"
    from_email = "noreply@alxtravelapp.com"
    
    send_mail(subject, message, from_email, [user_email])
    return "Email Sent"