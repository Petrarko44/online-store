from django.contrib import admin
from goods.models import Category, Subcategory, Type, Brand, Goods




class SubcategoryInline(admin.StackedInline):
    model = Subcategory
    extra = 1


class TypeInline(admin.StackedInline):
    model = Type
    extra = 1


class GoodsInline(admin.TabularInline):
    model = Goods
    extra = 1


class GoodsAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('title', 'category', 'brand', 'vendor_code',)
    list_filter = ('title', 'category', 'vendor_code', 'price', 'brand', 'category')
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'brand', 'vendor_code', 'quantity')
        }),
        ('Price', {
            'fields': ('price', 'discount')
        }),
        ('Full description', {
            'fields': ('description', 'characteristics', 'reviews')
        })
    )

    class Meta:
        model = Goods


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SubcategoryInline,]

    class Meta:
        model = Category


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    fields = ['title', 'category', 'brand']
    inlines = [TypeInline,]

    class Meta:
        model = Subcategory


class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    fields = ['title', 'category',]
    inlines = [GoodsInline, ]

    class Meta:
        model = Type


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ['title',]
    inlines = [GoodsInline, ]

    class Meta:
        model = Brand

admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand, BrandAdmin)