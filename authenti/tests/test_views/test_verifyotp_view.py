from rest_framework import test, status
from django.contrib.auth import get_user_model


User = get_user_model()


class VerifyotpViewTest(test.APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user1 = User.objects.create(
            username='user1',
            otp='123456',
            email='user1@dummymail.com'
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

    def test_incorrectotp_returnserror(self):
        data = self.get_verifyotp_data('user1', '111111')

        response = self.client.post('/auth/verifyotp', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'otp': ['Incorrect OTP']}
        )

    def test_usernamenotexists_returnserror(self):
        data = self.get_verifyotp_data('user2','123456')

        response = self.client.post('/auth/verifyotp', data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
            response.json(),
            {'detail': 'Not found.'}
        )

    def test_validinput_usercreated(self):
        data = self.get_verifyotp_data('user1', '123456')

        response = self.client.post('/auth/verifyotp', data=data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.json().get('username'), self.user1.username)
        self.assertIsNotNone(response.json().get('token'))
