import django_filters
from django_filters import rest_framework as filters

from carts.models import Cart

class CartFilter(filters.FilterSet):
    time_created__range = django_filters.DateTimeFromToRangeFilter(field_name='created_at', lookup_expr='range')
    
    class Meta:
        model = Cart
        fields = ['user', 'created_at', 'updated_at', 'product', 'quantity',]
