from django.contrib import admin
from restaurant.models import Restaurant, User, MenuItem, Order, OrderItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating', 'status', 'category', 'active')
    search_fields = ('name', 'address', 'category')
    list_filter = ('active', 'status', 'category')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'typology', 'active')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('typology', 'active')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'category', 'restaurant')
    search_fields = ('name', 'category', 'restaurant__name')
    list_filter = ('available', 'category', 'restaurant')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'restaurant', 'status', 'total_amount', 'created_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'restaurant__name', 'status')
    list_filter = ('status', 'created_at')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'order', 'quantity', 'subtotal', 'created_at')
    search_fields = ('menu_item__name', 'order__id')
    list_filter = ('created_at', 'order__restaurant')