from unittest import mock

from rest_framework import test, status
from django.contrib.auth import get_user_model


User = get_user_model()


class SigninViewTest(test.APITestCase):
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

    def get_signin_data(self, username, password, redirect_url='/'):
        return {
            'username': username,
            'password': password,
            'redirect_url': redirect_url
        }

    def test_usernotexists_returnsnotfounderror(self):
        data = self.get_signin_data('user2', 'somepass')

        response = self.client.post('/auth/signin', data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
            response.json(),
            {'detail': 'Not found.'}
        )

    def test_incorrectpassword_returnserror(self):
        data = self.get_signin_data('user1','wrongpassword')

        response = self.client.post('/auth/signin', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'password': ['Incorrect Password']}
        )

    def test_redirecturl_provided_redirectpathset(self):
        data = self.get_signin_data('user1', 'user1pass', 'someurl')
        response = self.client.post('/auth/signin', data=data)
        redirect_path = response._headers.get('location')[1]
        redirect_url = redirect_path.split('?')[1]
        self.assertEqual(
            redirect_url,
            'redirect_url={}'.format('someurl')
        )

    @mock.patch('authenti.tasks.send_otp_mail.run')
    def test_validinput_otpmailsent(self, send_otp_mail_mock):
        data = self.get_signin_data('user1', 'user1pass')
        response = self.client.post('/auth/signin', data=data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        send_otp_mail_mock.assert_called()
