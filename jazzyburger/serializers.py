from .models import Product
from rest_framework import serializers
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'image', 'count', 'cart')

class ProductDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'image', 'count', 'cart')
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
