# api/serializers.py

from rest_framework import serializers
from .models import Project, Page, Section, Component

class ComponentSerializer(serializers.ModelSerializer):
    """ Translates a single Component model into JSON. """
    class Meta:
        model = Component
        # Includes the new 'styles' and 'order' fields
        fields = ['id', 'component_type', 'content', 'styles', 'order']

class SectionSerializer(serializers.ModelSerializer):
    """ Translates a Section and nests all of its Components. """
    # This nests the ComponentSerializer, showing all components inside this section.
    components = ComponentSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'section_type', 'order', 'components']

class PageSerializer(serializers.ModelSerializer):
    """ Translates a Page and nests all of its Sections. """
    # This nests the SectionSerializer, creating a full page structure.
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'name', 'sections']

class ProjectDetailSerializer(serializers.ModelSerializer):
    """ 
    Translates a full Project, nesting all of its Pages.
    This is the main serializer our editor will use to get a complete website.
    """
    pages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'user', 'name', 'created_at', 'updated_at', 'pages']
        read_only_fields = ['user']

class ProjectListSerializer(serializers.ModelSerializer):
    """ 
    A simpler serializer for just listing project names, without all the detail.
    """
    class Meta:
        model = Project
        fields = ['id', 'name', 'updated_at']