from django.test import TestCase;
from restaurant.models import Menu;

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(ID=999, Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")