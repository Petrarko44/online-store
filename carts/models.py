from django.db import models
from django.conf import settings

from goods.models import Product, BaseModel

class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    quantity = models.PositiveSmallIntegerField(default=0,)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    
    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    objects = CartQuerySet().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Cart {self.user.username} Product {self.product.name} Quantity {self.quantity} Total {self.products_price()}'
        return f'Product {self.product.name} Quantity {self.quantity} Total {self.products_price()}'
