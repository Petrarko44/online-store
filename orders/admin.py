from django.contrib import admin
from orders.models import Order, OrderItem
from django.contrib.auth import get_user_model

admin.site.register(Order)
admin.site.register(OrderItem)
