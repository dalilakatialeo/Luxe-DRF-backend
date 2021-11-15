from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    make = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    engine = serializers.CharField(max_length=200)
    colour = serializers.CharField(max_length=200)
    image = serializers.URLField()
    rating = serializers.FloatField()
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class ProductDetailSerializer(ProductSerializer):
    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.price = validated_data.get('price', instance.price)
        instance.engine = validated_data.get('engine', instance.engine)
        instance.colour = validated_data.get('colour', instance.colour)
        instance.image = validated_data.get('image', 
        instance.image)
        rating = validated_data.get('rating', 
        instance.rating)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance