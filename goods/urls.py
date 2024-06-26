from django.urls import path, include
from goods.views import *
from goods.routers import router_category, router_brand, router_goods


app_name = 'goods'
urlpatterns = [
    path('api/v1/', include(router_goods.urls)),    
    path('api/v1/', include(router_category.urls)),
    path('api/v1/', include(router_brand.urls)),    
]

