from unittest import mock

from django.test import TestCase
from django.contrib.auth import get_user_model

from authenti import tasks


@mock.patch('django.core.mail.send_mail')
class SendOtpEmailTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user1',
            email='user1@dummymail.com',
        )
        self.otpuser = get_user_model().objects.create(
            username='user2',
            email='user2@dummymail.com',
            otp='123456'
        )

    def test_sendotpmail_usernotexists_mailnotsent(self, send_mail_mock):
        tasks.send_otp_mail(3)
        send_mail_mock.assert_not_called()

    def test_sendotpmail_userotpnotset_mailnotsent(self, send_mail_mock):
        tasks.send_otp_mail(self.user.id)
        send_mail_mock.assert_not_called()

    def test_sendotpmail_userotpset_mailsent(self, send_mail_mock):
        tasks.send_otp_mail(self.otpuser.id)
        send_mail_mock.assert_called_once()
