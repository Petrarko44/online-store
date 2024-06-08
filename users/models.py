from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, AbstractUser, UserManager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Email is the default for authentication instead of the username
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,  password=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user

    # def get_by_natural_key(self, username):
    #     if '@' in username:
    #         return self.get(email=username)
    #     else:
    #         return self.get(username=username)


class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    detail_address = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

