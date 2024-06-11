from django.contrib import admin

from carts.models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'session_key', 'time_created')
    list_filter = ('user', 'product', 'quantity', 'session_key', 'time_created')    
    
    
admin.site.register(Cart, CartAdmin)