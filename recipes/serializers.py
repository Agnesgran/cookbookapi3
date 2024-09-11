from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ['id', 'owner', 'name', 'ingredients', 'instructions', 'category', 'created_at', 'updated_at']
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Recipe name must be at least 3 characters long.")
        return value