from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('list/', UserListView.as_view(), name='user_list'),
]