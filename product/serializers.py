from rest_framework import serializers

from .models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    
    class Meta:
        model = Product
        fields = ('name', 'image', 'category')


class ProductDetailSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'