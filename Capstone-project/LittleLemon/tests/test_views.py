from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="tester", password="Pass123#")
        self.token = Token.objects.create(user=self.user)

        # Create a few test Menu instances
        self.item1 = Menu.objects.create(Title="Pasta", Price=12.50, Inventory=10)
        self.item2 = Menu.objects.create(Title="Pizza", Price=15.00, Inventory=5)
        self.item3 = Menu.objects.create(Title="Salad", Price=8.00, Inventory=20)

        # Initialize APIClient for making requests
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_getall(self):
        # Call the MenuItemsView endpoint
        url = reverse('menu_items')  # assumes you named the URL pattern 'menu-items'
        response = self.client.get(url)

        # Get all Menu objects from DB
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert response matches serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)