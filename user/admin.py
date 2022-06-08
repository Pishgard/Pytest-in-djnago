from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import *
# change admin header
admin.site.site_header = "پنل مدیریت سرنخ"

admin.autodiscover()


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    model = get_user_model()
    actions = ['delete_selected']

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_superuser', 'email_verified', 'phone_verified')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('phone', 'password', 'email')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email_verified', 'phone_verified', 'sms_notif', 'email_notif', 'active')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')}
         ),
    )
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('phone',)

    def full_name(self, obj):
        return obj.get_full_name()

    def get_phone_number(self, obj):
        if obj.phone_number:
            return obj.phone_number.as_national.replace(" ", "-")
        return None

    def delete_model(self, request, obj):
        obj.delete()
        super(CustomUserAdmin, self).delete_model(self, request, obj)

    def delete_selected(modeladmin, request, queryset):
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = "Delete selected Users"

    get_phone_number.short_description = 'شماره تلفن همراه'
    get_phone_number.admin_order_field = 'phone'