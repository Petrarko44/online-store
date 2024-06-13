from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from carts.serializers import CartSerializer

from carts.filters import CartFilter
from rest_framework.permissions import IsAdminUser

from carts.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CartFilter
    permission_classes = (IsAdminUser,)
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]