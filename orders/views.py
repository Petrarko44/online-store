from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from orders.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from orders.filters import OrderFilter, OrderItemFilter
from orders.models import Order, OrderItem
from orders.serializers import OrderItemSerializer, OrderSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication,]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderItemFilter
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication,]