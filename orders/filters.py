import django_filters
from django_filters import rest_framework as filters

from orders.models import Order, OrderItem

class OrderFilter(filters.FilterSet):
    created_at__range = django_filters.DateTimeFromToRangeFilter(field_name='created_at', lookup_expr='range')  

    class Meta:
        model = Order
        fields = ['user', 'created_at', 'delivery', 'delivery_date', 'payment', 'is_paid', 'status']

class OrderItemFilter(filters.FilterSet):
    created_at__range = django_filters.DateTimeFromToRangeFilter(field_name='created_at', lookup_expr='range')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = OrderItem
        fields = ['order', 'created_at', 'name', 'price', 'quantity']
    