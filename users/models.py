from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from goods.models import Type


class NewUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        username = f'{self.first_name} {self.last_name}'
        return username

# тут лежит ковыряние в админке

# class GoodsAdmin(admin.ModelAdmin):
#     list_filter = ('title', 'category', 'vendor_code', 'price')
#     # fields = ['title', 'category', ('vendor_code', 'price')]
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'category', 'vendor_code', 'price')
#         }),
#         ('Полное описание', {
#             'fields': ('description', 'characteristics')
#         })
#     )
# @admin.register(Type)
# class TypeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'display_brand')
#     fields = ['title', ('category', 'display_brand')]

