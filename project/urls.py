from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API List",
      default_version='v1',
      description="Develop Level",
      terms_of_service="https://AliCode.ir/",
      contact=openapi.Contact(email="Ali.Pishgard79@gmail.com"),
      license=openapi.License(name="Develop Level License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls', namespace='produt')),
    path('user/', include('user.urls', namespace='user')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)