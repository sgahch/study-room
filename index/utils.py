from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(student_email, subject, message):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [student_email],
            fail_silently=False,
        )
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")