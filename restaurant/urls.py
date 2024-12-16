from django.urls import path
from rest_framework.routers import DefaultRouter
from restaurant.views import RestaurantViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')

urlpatterns = router.urls