from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import exceptions

from authenti.api import serializers


User = get_user_model()


class SigninSerializerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user1 = User.objects.create(
            username='user1',
            email='user1@dummymail.com'
        )
        cls.user1.set_password('user1pass')
        cls.user1.save()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        User.objects.all().delete()

    def get_signin_data(self, username, password):
        return {
            'username': username,
            'password': password,
        }

    def test_validate_incorrectpassword_raisesexception(self):
        data = self.get_signin_data('user1', 'somepass')

        serializer = serializers.SigninSerializer(data=data,
                                                  instance=self.user1)
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_save_otpset(self):
        data = self.get_signin_data('user1', 'user1pass')

        serializer = serializers.SigninSerializer(data=data,
                                                  instance=self.user1)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.user1.refresh_from_db()
        self.assertIsNotNone(self.user1.otp)
