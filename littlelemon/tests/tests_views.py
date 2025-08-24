from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=12, inventory=10)
        Menu.objects.create(title="Burger", price=8, inventory=20)
        Menu.objects.create(title="Pasta", price=10, inventory=15)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 3)