from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ManyToManyField(Brand, related_name='subcategor')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.ManyToManyField(Brand, related_name='types')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'

    def __str__(self):
        return self.title


class Goods(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Название')
    # slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    category = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Категория', related_name='type')
    vendor_code = models.CharField(max_length=150, blank=True, null=True, verbose_name='Артикул')
    # image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    characteristics = models.TextField(blank=True, null=True, verbose_name='Характеристики') #можно замутить класс характеристики
    reviews = models.TextField(blank=True, null=True, verbose_name='Отзывы')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')

    class Meta:
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}\nАртикул: {self.vendor_code}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        return self.price

    def status_availability(self):
        if self.quantity >= 1:
            return f'В наличии.'
        return f'Нет в наличии.'