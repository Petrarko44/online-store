from django.urls import path, include

from orders.routers import router_orders, router_orders_item


app_name = 'orders'
urlpatterns = [
    path('api/v1/', include(router_orders.urls)),
    path('api/v1/', include(router_orders_item.urls)),    
]

