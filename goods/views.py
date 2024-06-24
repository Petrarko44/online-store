from django.shortcuts import render
from rest_framework import viewsets

from goods.models import Product, Category, Brand
from goods.serializers import ProductSerializer, CategorySerializer, BrandSerializer
from django_filters.rest_framework import DjangoFilterBackend
from goods.filters import GoodsFilter
from goods.permissions import IsAdminOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GoodsFilter
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]