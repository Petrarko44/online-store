from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title

    def display_brand(self):
        return ', '.join([brand.title for brand in self.brand.all()[:3]])

    display_brand.short_description = 'brand'


class Subcategory(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ManyToManyField(Brand, related_name='subcategor', blank=True)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.ManyToManyField(Brand, related_name='types')

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.title

    def display_brand(self):
        return ', '.join([brand.title for brand in self.brand.all()[:3]])

    display_brand.short_description = 'brand'


class Goods(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Name')
    category = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Category', related_name='type')
    vendor_code = models.CharField(max_length=150, blank=True, null=True, verbose_name='Vendor code')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    characteristics = models.TextField(
        blank=True, null=True, verbose_name='Characteristics',
    )  # можно замутить класс характеристики
    reviews = models.TextField(blank=True, null=True, verbose_name='Reviews')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Discount %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='Brand')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='User')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.title}\nVendor code: {self.vendor_code}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def status_availability(self):
        if self.quantity >= 1:
            return f'available.'
        return f'Not available.'
