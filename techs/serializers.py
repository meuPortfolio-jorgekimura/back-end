from rest_framework import serializers
from .models import Tech


class TechSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        tech, _ = Tech.objects.get_or_create(**validated_data)
        return tech

    class Meta:
        model = Tech
        fields = [
            "id",
            "name",
            "img_url"
        ]
