from rest_framework import serializers
from rest_framework.permissions import  IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

# Register serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=('id','username','password','first_name','last_name')
#         extra_kwargs={'password':{'write_only':True},}
#
#         def create(self,validated_data):
#             user=User.objects.create_user(validated_data['username'],
#                                           password=validated_data['password'],
#                                           first_name=validated_data['first_name'],
#                                           last_name=validated_data['last_name'])
#             return user
#
# #User serializer
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email','password','first_name','last_name')

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=('email','password','first_name','last_name')

    def create(self,validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name',''),
        )
        return user

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

    def validate(self, attrs):
        user=authenticate(email=attrs['email'],password=attrs['password'])
        if not user:
            raise serializers.ValidationError('invalid email or password')
        attrs['user']=user
        return attrs

    def to_representation(self, instance):
        response_data=super().to_representation(instance)
        refresh=RefreshToken.for_user(instance)
        response_data['access_token']=str(refresh.access_token)
        response_data['refresh_token'] = str(refresh)
        response_data['user_id'] = instance.id
        return response_data