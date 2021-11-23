<<<<<<< HEAD
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class UserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
=======
from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser(
            email= validated_data["email"],
            username= validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

#update user details - name and email

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
>>>>>>> main
        instance.save()
        return instance