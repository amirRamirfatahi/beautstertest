from rest_framework import test, status
from django.contrib.auth import get_user_model


User = get_user_model()


class SignupViewTest(test.APITestCase):
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

    def test_usernameexists_returnserror(self):
        data = self.get_signup_data('user1', 'somepass', 'user2@dummy.com')

        response = self.client.post('/auth/signup/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'username': ['user with this username already exists.']}
        )

    def test_emailexists_returnserror(self):
        data = self.get_signup_data('user2','somepass','user1@dummymail.com')

        response = self.client.post('/auth/signup/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {'email': ['user with this email already exists.']}
        )

    def test_usernameandemailexists_returnserror(self):
        data = self.get_signup_data('user1', 'somepass', 'user1@dummymail.com')

        response = self.client.post('/auth/signup/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                'username': ['user with this username already exists.'],
                'email': ['user with this email already exists.']
            }
        )

    def test_validinput_usercreated(self):
        data = self.get_signup_data('user2', 'somepass', 'user2@dummy.com')

        response = self.client.post('/auth/signup/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data.pop('password')
        self.assertEqual(response.json(), data)
