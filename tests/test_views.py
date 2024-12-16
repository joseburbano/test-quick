from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Restaurant

class RestaurantViewSetTest(APITestCase):
    def test_create_restaurant(self):
        data = {"name": "Test Restaurant", "address": "123 Test Street"}
        response = self.client.post('/api/restaurants/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_restaurants(self):
        Restaurant.objects.create(name="Test Restaurant", address="123 Test Street")
        response = self.client.get('/api/restaurants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)