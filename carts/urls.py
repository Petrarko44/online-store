from django.urls import path, include
from carts.routers import router_cart


app_name = 'carts'
urlpatterns = [
    path('api/v1/', include(router_cart.urls)),   
]
