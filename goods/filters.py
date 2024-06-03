import django_filters
from django_filters import rest_framework as filters
from goods.models import Goods

class GoodsFilter(filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    brand__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price', 'brand']