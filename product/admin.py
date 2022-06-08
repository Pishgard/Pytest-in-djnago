from django.contrib import admin
from .models import *

admin.site.site_header = "پنل مدیریت فروشگاه آزمون نرم افزار"

admin.autodiscover()

admin.site.register(Category)
admin.site.register(Product)
