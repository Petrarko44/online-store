from rest_framework import routers

from carts.views import CartViewSet


router_cart = routers.SimpleRouter()
router_cart.register(r'cart', CartViewSet)
