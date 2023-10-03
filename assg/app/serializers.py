from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password'] 
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','body','author']