from django.test import TestCase, Client

from django.urls import reverse

from taxi.forms import ManufacturerSearchForm
from taxi.models import Manufacturer


class SearchTest(TestCase):
    def test_search_manufacturer(self):
        client = Client()
        response = client.get(reverse("taxi:driver-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["search_form"], ManufacturerSearchForm)

    def test_search_manufacturer_filtering(self):
        Manufacturer.objects.create(name="BMW", country="Germany")
        Manufacturer.objects.create(name="Ferrari", country="Italy")

        client = Client()
        response = client.get(reverse("taxi:driver-list"), {"name": "BMW"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BMW")
        self.assertNotContains(response, "Ferrari")
