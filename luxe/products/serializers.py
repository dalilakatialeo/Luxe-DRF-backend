from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    make = serializers.CharField(max_length=200)
    car_model = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    engine = serializers.CharField(max_length=200)
    body_type = serializers.CharField(max_length=200)
    fuel = serializers.CharField(max_length=200)
    colour = serializers.CharField(max_length=200)
    url = serializers.URLField()
    image = serializers.URLField()
    

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class ProductDetailSerializer(ProductSerializer):
    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.car_model = validated_data.get('car_model', instance.car_model)
        instance.price = validated_data.get('price', instance.price)
        instance.engine = validated_data.get('engine', instance.engine)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.body_type = validated_data.get('body_type', instance.body_type)
        instance.colour = validated_data.get('colour', instance.colour)
        instance.image = validated_data.get('image', instance.image)
        instance.url = validated_data.get('url', instance.url)
    
        instance.save() 
        return instance