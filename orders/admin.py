from django.contrib import admin

from orders.models import Order, OrderItem

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1
    

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity', 'created_at')
    list_filter = ('order', 'product', 'price', 'quantity', 'created_at')    

    class Meta:
        model = OrderItem
  

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,]
    list_display = ('user', 'created_at', 'phone_number', 'delivery', 'delivery_address', 'delivery_date', 'payment', 'is_paid', 'status')
    list_filter = ('user', 'created_at', 'phone_number', 'delivery', 'delivery_address', 'delivery_date', 'payment', 'is_paid', 'status')  
    fieldsets = (
        (None, {
            'fields': ('user', 'phone_number',)
        }),
        ('Delivery info', {
            'fields': ('delivery', 'delivery_address', 'delivery_date')
        }),
        ('Payment', {
            'fields': ('payment', 'is_paid', 'status')
        })
    )  

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
