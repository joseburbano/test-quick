from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=21, decimal_places=11, null=True, blank=True)
    longitude = models.DecimalField(max_digits=21, decimal_places=11, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    active = models.BooleanField(default=True)  # Activo/inactivo

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"


class User(models.Model):
    RESTAURANT_CHOICES = [
        ('dealer', 'Dealer'),
        ('customer', 'Customer'),
    ]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    default_address = models.TextField(null=True, blank=True)
    typology = models.CharField(max_length=20, choices=RESTAURANT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    special_instructions = models.TextField(null=True, blank=True)
    estimated_delivery_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.first_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item {self.menu_item.name} - Order {self.order.id}"