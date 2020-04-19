from beautstertest.celery import app
from django.conf import settings


@app.task()
def send_otp_mail(user_id):
    from django.contrib.auth import get_user_model
    from django.core.mail import send_mail

    from authenti.constants import OTP_EMAIL_TEMPLATE, OTP_SEND_MAIL_KWARGS

    user = get_user_model().objects.filter(id=user_id).first()


    if not user or not user.otp:
        return

    send_mail(
        message=OTP_EMAIL_TEMPLATE.format(username=user.username,
                                          otp=user.otp),
        recipient_list=[user.email],
        **OTP_SEND_MAIL_KWARGS
    )
