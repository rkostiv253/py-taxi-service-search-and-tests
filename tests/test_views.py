from django.test import TestCase, Client

from django.urls import reverse

from taxi.forms import ManufacturerSearchForm

def test_search_manufacturer(self):
    client = Client()
    response = client.get(reverse('taxi.views.DriverListView'))
    self.assertEquals(response.status_code, 200)
    self.assertIsInstance(response.context['form'], ManufacturerSearchForm)