from django.contrib import admin
from goods.models import Category, Subcategory, Type, Brand, Product


class SubcategoryInline(admin.StackedInline):
    model = Subcategory
    extra = 1


class TypeInline(admin.StackedInline):
    model = Type
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
    inlines = [SubcategoryInline,]

    class Meta:
        model = Category


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    fields = ['name', 'category']
    inlines = [TypeInline,]

    class Meta:
        model = Subcategory


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory',)
    fields = ['name', 'subcategory',]
    inlines = [ProductInline, ]

    class Meta:
        model = Type


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['name',]
    inlines = [ProductInline, ]

    class Meta:
        model = Brand


admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand, BrandAdmin)