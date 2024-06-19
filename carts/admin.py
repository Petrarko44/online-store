from django.contrib import admin

from carts.models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'session_key', 'created_at', 'updated_at',)
    list_filter = ('user', 'product', 'quantity', 'session_key', 'created_at', 'updated_at',)    
    
    class Meta:
        model = Cart
    
admin.site.register(Cart, CartAdmin)