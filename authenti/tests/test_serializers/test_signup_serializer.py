from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import exceptions

from authenti.api import serializers


User = get_user_model()


class SignupSerializerTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(
            username='user1',
            email='user1@dummymail.com'
        )

    def get_signup_data(self, username, password, email):
        return {
            'username': username,
            'password': password,
            'email': email
        }

    def test_validate_usernameexists_raisesexception(self):
        data = self.get_signup_data('user1', 'somepass', 'user2@dummymail.com')

        serializer = serializers.SignupSerializer(data=data)
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_validate_emailexists_raisesexception(self):
        data = self.get_signup_data('user2', 'somepass', 'user1@dummymail.com')

        serializer = serializers.SignupSerializer(data=data)
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_validate_uniquedata_usercreated(self):
        data = self.get_signup_data('user2', 'somepass', 'user2@dummymail.com')

        serializer = serializers.SignupSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertTrue(User.objects.filter(username='user2').exists())
