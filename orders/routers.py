from rest_framework import routers
from orders.views import OrderViewSet, OrderItemViewSet


router_orders = routers.SimpleRouter()
router_orders.register(r'orders', OrderViewSet)

router_orders_item = routers.SimpleRouter()
router_orders_item.register(r'orders_item', OrderItemViewSet)