import os
import csv
import json

from django.db import models
from django.conf import settings

from goods.models import Goods


class OrderItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, null=True, blank=True, verbose_name='User',default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Order creation date')
    phone_number = models.CharField(max_length=9, verbose_name='Phone number')
    DELIVERY_METHOD = [
        ("Courier", "Delivery by courier at a time convenient for you"),
        ("Pickup", "Pickup, Minsk, Nemanskaya 20"),
        ("Post", "Delivery by post to the address you provide"),
    ]
    delivery = models.CharField(max_length=10, choices=DELIVERY_METHOD, verbose_name='Delivery method')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Delivery address')
    delivery_date = models.DateField()
    PAYMENT_METHOD = [
        ("Cash", "By cash"),
        ("Card", "By card"),
        ("Online", "Online payment"),
    ]
    payment = models.CharField(max_length=40, choices=PAYMENT_METHOD, verbose_name='Payment method')
    is_paid = models.BooleanField(default=False, verbose_name='Paid')
    status = models.CharField(max_length=50, default='in processing', verbose_name='Order status')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order № {self.pk} | Buyer {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(Goods,on_delete=models.SET_DEFAULT, null=True, verbose_name='Product', default=None)
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Name')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date of sale')

    class Meta:
        verbose_name = 'Sold item'
        verbose_name_plural = 'Sold items'

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Item {self.title} | Order № {self.order.pk}"