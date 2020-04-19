from django.conf import settings

OTP_LENGTH = 6

OTP_EMAIL_TEMPLATE = """
dear {username},
Following is your one time password:
    {otp}
"""

OTP_SEND_MAIL_KWARGS = {
    'subject': 'beautster otp',
    'from_email': f'{{ settings.ADMIN_EMAIL }}'
}
