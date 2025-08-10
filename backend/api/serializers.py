# api/serializers.py

from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    This serializer will translate the Project model into a JSON format.
    """

    class Meta:
        # The model we want to translate
        model = Project
        
        # The specific fields we want to include in the JSON output
        fields = ['id', 'user', 'name', 'created_at', 'updated_at']
        
        # We make the 'user' field read-only to prevent it from being
        # changed via the API. The user will be set automatically based on
        # who is logged in.
        read_only_fields = ['user']