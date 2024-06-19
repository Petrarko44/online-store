import django_filters
from django_filters import rest_framework as filters
from goods.models import Product

class GoodsFilter(filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    
    class Meta:
        model = Product
        fields = ['price', 'brand', 'type', ]
