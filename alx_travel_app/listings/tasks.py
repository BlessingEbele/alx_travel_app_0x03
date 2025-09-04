from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(to_email, booking_details):
    subject = "Booking Confirmation"
    message = (
        f"Hello, your booking was successful!\n\n"
        f"Booking Details:\n"
        f"Booking ID: {booking_details.get('booking_id')}\n"
        f"Destination: {booking_details.get('destination', 'N/A')}\n"
        f"Date: {booking_details.get('date', 'N/A')}\n"
    )
    from_email = "webmaster@localhost"
    send_mail(subject, message, from_email, [to_email])
    return f"Email sent to {to_email}"

