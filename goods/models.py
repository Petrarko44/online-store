import uuid

from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
     
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Brand(BaseModel):
    
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name

    def display_brand(self):
        return ', '.join([brand.name for brand in self.brand.all()[:3]])

    display_brand.short_description = 'brand'


class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name


class Type(BaseModel):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.name
      

class Product(BaseModel):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')
    vendor_code = models.CharField(max_length=150, blank=True, null=True, verbose_name='vendor code')
    description = models.TextField(blank=True, null=True)
    characteristics = models.TextField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True, verbose_name='reviews')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='price')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='discount %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='brand')
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'{self.name}\nVendor code: {self.vendor_code}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def status_availability(self):
        if self.quantity >= 1:
            return f'available.'
        return f'Not available.'


class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.name}'s {self.name} on {self.product.name}"

    class Meta:
        ordering = ['rating']