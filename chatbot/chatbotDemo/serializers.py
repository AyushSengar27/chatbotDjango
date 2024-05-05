from rest_framework import serializers
from .models import UserPrompt

class UserPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPrompt
        fields = ('username', 'prompt')

class UserResponseSerializer(serializers.Serializer):
    response = serializers.CharField()