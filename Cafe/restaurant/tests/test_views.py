from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(Title="Spaghetti", Price=10.99, ID = 56, Inventory=10)
        self.menu2 = Menu.objects.create(Title="Salad", Price=5.99, ID = 57, Inventory=10)
        self.menu3 = Menu.objects.create(Title="Soup", Price=4.99, ID = 58, Inventory=10)

    def test_getall(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='password')

        # Authenticate the client with the created user
        self.client.force_login(user)

        # Make a GET request to the 'menu-list' endpoint
        response = self.client.get(reverse('menu-list'))

        # Ensure the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the database objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Compare the serialized data with the response data
        self.assertEqual(response.data, serializer.data)
