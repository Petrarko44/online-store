from django.db import models
from goods.models import Goods
from django.conf import settings


class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, )
    product = models.ForeignKey(Goods, on_delete=models.CASCADE, )
    quantity = models.PositiveSmallIntegerField(default=0,)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    objects = CartQuerySet().as_manager

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Cart {self.user.username} Product {self.product.title} Quantity {self.quantity} Total {self.products_price()}'
        return f'Product {self.product.title} Quantity {self.quantity} Total {self.products_price()}'
