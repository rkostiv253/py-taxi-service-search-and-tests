from django.test import TestCase, Client

from django.urls import reverse

from taxi.forms import ManufacturerSearchForm


class SearchTest(TestCase):
    def test_search_manufacturer(self):
        client = Client()
        response = client.get(reverse("taxi:driver-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], ManufacturerSearchForm)
