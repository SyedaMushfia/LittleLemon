from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Pizza", price=150, inventory=20)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        items = MenuItem.objects.all()
        serialized_items = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_items.data)
