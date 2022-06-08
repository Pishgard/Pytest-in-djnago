from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from rest_framework.response import Response

from .models import *
from .serializers import *


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(generics.UpdateAPIView):
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'

    def get(self, request, id):
        exam = get_object_or_404(Product, id=id)
        serializer = self.serializer_class(exam)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer



class ProductCategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()
