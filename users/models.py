from django.db import models
from django.contrib.auth.models import AbstractUser


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