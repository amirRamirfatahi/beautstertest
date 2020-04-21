from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import exceptions

from authenti.api import serializers


User = get_user_model()


class VerifyotpSerializerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user1 = User.objects.create(
            username='user1',
            email='user1@dummymail.com',
            otp='123456'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        User.objects.all().delete()

    def get_verifyotp_data(self, username, otp, redirect_url='/'):
        return {
            'username': username,
            'otp': otp,
            'redirect_url': redirect_url
        }

    def test_validate_incorrectotp_raisesexception(self):
        data = self.get_verifyotp_data('user1', '111111')

        serializer = serializers.VerifyotpSerializer(data=data,
                                                     instance=self.user1)
        with self.assertRaises(exceptions.ValidationError):
           serializer.is_valid(raise_exception=True)

    def test_save_tokenset(self):
        data = self.get_verifyotp_data('user1', '123456')

        serializer = serializers.VerifyotpSerializer(data=data,
                                                     instance=self.user1)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.user1.refresh_from_db()
        self.assertIsNotNone(self.user1.token)
