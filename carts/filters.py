import django_filters
from django_filters import rest_framework as filters

from carts.models import Cart

class CartFilter(filters.FilterSet):
    time_created__range = django_filters.DateTimeFromToRangeFilter(field_name='time_created', lookup_expr='range')
    
    class Meta:
        model = Cart
        fields = ['user', 'time_created', 'product', 'quantity',]
