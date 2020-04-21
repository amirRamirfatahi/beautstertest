from unittest import mock

from rest_framework.test import APITestCase
from django.http import HttpRequest
from django.shortcuts import reverse

from salon.models import Salon
from salon.utils import filters
from salon.api.views import listsalon_view


class SalonListViewTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.custom_view = listsalon_view
        cls.base_url = reverse('salon:salons')
        names = ['abcde', 'abcda', 'abcab', 'ababc']
        salons = []
        for name in names:
            salons.append(Salon(name=name))
        Salon.objects.bulk_create(salons)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        Salon.objects.all().delete()

    def get_url_with_param(self, searchkey):
        return '{base}?tgsearch={searchkey}'.format(
            base=self.base_url,
            searchkey=searchkey
        )

    @mock.patch('salon.api.views.salons_list_view.ListSalonsView.' \
                'tgsearch_threshold', new_callable=mock.PropertyMock,
                return_value=0.5)
    def test_tgsearch_qparamgiven_similarsreturned(self, listsalon_view_mock):
        response = self.client.get(self.base_url)
        self.assertEqual(len(response.json()), 4)

        url = self.get_url_with_param('abcd')
        response = self.client.get(url)
        self.assertEqual(len(response.json()), 2)
        self.assertListEqual(
            response.json(),
            [{'id': 1, 'name': 'abcde'}, {'id': 2, 'name': 'abcda'}]
        )

