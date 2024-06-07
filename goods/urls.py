from django.urls import path, include
from goods.views import *
from goods.routers import router_category, router_subcategory, router_type, router_brand, router_goods


app_name = 'goods'
urlpatterns = [
    path('api/v1/', include(router_goods.urls)),
    # path('api/v1/goods/', GoodsAPIList.as_view()),
    path('api/v1/', include(router_category.urls)),
    path('api/v1/', include(router_subcategory.urls)),
    path('api/v1/', include(router_type.urls)),
    path('api/v1/', include(router_brand.urls)),
    # path('api/v1/subcategory/', SubcategoryAPIList.as_view()),
    # path('api/v1/subcategory/<int:pk>/', SubcategoryAPIDetail.as_view())
]

