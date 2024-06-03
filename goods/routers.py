from rest_framework import routers
from goods.views import GoodsViewSet, CategoryViewSet, SubcategoryViewSet, TypeViewSet, BrandViewSet


router_goods = routers.SimpleRouter()
router_goods.register(r'goods', GoodsViewSet)

router_category = routers.SimpleRouter()
router_category.register(r'category', CategoryViewSet)

router_subcategory = routers.SimpleRouter()
router_subcategory.register(r'subcategory', SubcategoryViewSet)

router_type = routers.SimpleRouter()
router_type.register(r'type', TypeViewSet)

router_brand = routers.SimpleRouter()
router_brand.register(r'brand', BrandViewSet)