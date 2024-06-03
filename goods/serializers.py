from rest_framework import serializers
from goods.models import Goods, Subcategory, Category, Type, Brand


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'