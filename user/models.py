from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import (AbstractUser, BaseUserManager, PermissionsMixin)


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if email is None:
            raise TypeError("Users should have a Email")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if password is None:
            raise TypeError("Password should not be None")

        user = self.create_user(email, password, **extra_fields)
        user = self.model(email=self.normalize_email(email))
        return user


class User(AbstractUser):
    email = models.EmailField('آدرس ایمیل', max_length=255, unique=True, null=True, blank=True)
    email_verified = models.BooleanField('معتبر بودن ایمیل', default=False)
    phone = PhoneNumberField('شماره موبایل', unique=True, null=True, blank=True)
    phone_verified = models.BooleanField('معتبر بودن شماره', default=False)

    sms_notif = models.BooleanField(default=False)
    email_notif = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)
    deleted_at = models.DateTimeField('تاریخ حذف', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        if self.get_full_name():
            name = self.get_full_name()
        else:
            name = self.email
        return name

    def __str__(self):
        return f"{self.phone}"

    # Return tokens of user
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'