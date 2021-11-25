from rest_framework import serializers
from .models import SavedRecommendation

class SavedRecommendationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    product_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return SavedRecommendation.objects.create(**validated_data)

class SavedRecommendationDetailSerializer(SavedRecommendationSerializer):
    def update(self, instance, validated_data):
        instance.product_id = validated_data.get('product_id', instance.make)
        instance.user_id = validated_data.get('user_id', instance.car_model)
    
        instance.save() 
        return instance