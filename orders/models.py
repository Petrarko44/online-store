from django.db import models
from django.conf import settings

from goods.models import Product, BaseModel


class OrderItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(BaseModel):     
    phone_number = models.CharField(max_length=9, verbose_name='phone number')
    DELIVERY_METHOD = [
        ("Courier", "Delivery by courier at a time convenient for you"),
        ("Pickup", "Pickup, Minsk, Nemanskaya 20"),
        ("Post", "Delivery by post to the address you provide"),
    ]
    delivery = models.CharField(max_length=10, choices=DELIVERY_METHOD, verbose_name='delivery method')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='delivery address')
    delivery_date = models.DateField()
    PAYMENT_METHOD = [
        ("Cash", "By cash"),
        ("Card", "By card"),
        ("Online", "Online payment"),
    ]
    payment = models.CharField(max_length=40, choices=PAYMENT_METHOD, verbose_name='payment method')
    is_paid = models.BooleanField(default=False, verbose_name='is paid')
    status = models.CharField(max_length=50, default='in processing', verbose_name='order status')

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return f"Order № {self.pk} | Buyer {self.user.first_name} {self.user.last_name}"


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.SET_DEFAULT,
                                 null=True, verbose_name='product', default=None)    
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='price')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    
    class Meta:
        verbose_name = 'sold item'
        verbose_name_plural = 'sold items'

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Item {self.name} | Order № {self.order.pk}"