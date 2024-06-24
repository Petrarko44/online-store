from rest_framework import routers
from goods.views import CategoryViewSet, BrandViewSet, GoodsViewSet


router_goods = routers.SimpleRouter()
router_goods.register(r'goods', GoodsViewSet)

router_category = routers.SimpleRouter()
router_category.register(r'category', CategoryViewSet)

router_brand = routers.SimpleRouter()
router_brand.register(r'brand', BrandViewSet)