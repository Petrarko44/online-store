from django.contrib import admin
from goods.models import Category, Brand, Product, Review


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class ProductAdmin(admin.ModelAdmin):    
    list_display = ('name', 'type', 'brand', 'vendor_code',)
    list_filter = ('name', 'type', 'vendor_code', 'price', 'brand')
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'brand', 'vendor_code', 'quantity')
        }),
        ('Price', {
            'fields': ('price', 'discount')
        }),
        ('Full description', {
            'fields': ('description', 'characteristics')
        })
    )

    class Meta:
        model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CategoryInline, ProductInline,]
   
    class Meta:
        model = Category


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['name',]
    inlines = [ProductInline, ]

    class Meta:
        model = Brand

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'product', 'rating', 'comment',)
    list_filter = ('name', 'user', 'product', 'rating', 'comment',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Review, ReviewAdmin)