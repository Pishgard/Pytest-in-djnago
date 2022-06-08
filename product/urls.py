from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('category/', ProductCategoryListView.as_view(), name='category_list'),
    path('category/create/', ProductCategoryCreateView.as_view(), name='category_create'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('<int:id>/', ProductDetailView.as_view(), name='product_detail'),
]