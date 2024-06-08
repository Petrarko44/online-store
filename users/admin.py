from django.contrib import admin
from django.conf import settings
# from users.models import NewUser

admin.register(settings.AUTH_USER_MODEL)
