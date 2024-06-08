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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, null=True, blank=True, verbose_name='Пользователь',default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    phone_number = models.CharField(max_length=9, verbose_name='Номер телефона')
    DELIVERY_METHOD = [
        ("Курьер", "Доставка курьером в удобное для Вас время"),
        ("Самовывоз", "Самовывоз г.Минск, Неманская 20"),
        ("Белпочта", "Доставка Белпочтой на указанный Вами адрес"),
    ]
    delivery = models.CharField(max_length=10, choices=DELIVERY_METHOD, verbose_name='Метод доставки')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    delivery_date = models.DateField()
    PAYMENT_METHOD = [
        ("Нал", "Наличными средствами"),
        ("Карта", "Банковской картой"),
        ("Онлайн", "Оплата онлайн"),
    ]
    payment = models.CharField(max_length=40, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=50, default='В обработке', verbose_name='Статус заказа')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Goods,on_delete=models.SET_DEFAULT, null=True, verbose_name='Товар', default=None)
    title = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')

    class Meta:
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.title} | Заказ № {self.order.pk}"