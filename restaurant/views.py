from rest_framework.viewsets import ModelViewSet
from restaurant.models import (Restaurant)
from restaurant.serializers import RestaurantSerializer

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer