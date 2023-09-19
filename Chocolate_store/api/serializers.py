from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Chocolate,Cart

class ChocoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chocolate
        fields='__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'