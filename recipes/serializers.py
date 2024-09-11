from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at',
            'name', 'ingredients', 'instructions', 'category'
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner
