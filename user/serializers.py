from .models import User
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'password', 'tokens')

    def get_tokens(self, obj):
        """A method for returning the tokens"""

        user = User.objects.get(email=obj['email'])

        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        # Add recently
        filtered_user_by_email = User.objects.filter(email=email)

        user = auth.authenticate(email=email, password=password)


        if not user:
            raise AuthenticationFailed('Invalid Credentials, try agian!')
        if not user.active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.email_verified:
            raise AuthenticationFailed('Email is not verified')
        return {
            'email': user.email,
            'tokens': user.tokens()
        }


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
