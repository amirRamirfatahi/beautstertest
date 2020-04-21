from rest_framework import status, test
from django.contrib.auth import get_user_model
from salon.models import Salon


User = get_user_model()


class BookingViewTest(test.APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            id=1,
            username='user1',
            email='user1@dummy.com',
            token='sometoken'
        )
        cls.salon = Salon.objects.create(name='salon one')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        User.objects.all().delete()
        Salon.objects.all().delete()

    def signin_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)

    def test_book_salongiven_bookingcreatedforuser(self):
        data = {'salon': 1}
        self.signin_user()
        response = self.client.post('/booking/', data=data)
        self.assertDictEqual(
            response.json(),
            {'user': 1, 'salon': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

