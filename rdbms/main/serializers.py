from rest_framework import serializers
from .models import Films

class FilmsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    length_min = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Films.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.length_min = validated_data.get('length_min', instance.length_min)
        instance.save()
        return instance
    
    