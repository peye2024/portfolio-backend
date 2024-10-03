from rest_framework import serializers

from coreapp.models import Document
from project.models import Tag, Project


class ProjectDocumentSerializer(serializers.ModelSerializer):
    document_url = serializers.CharField(source='get_url', read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'document_url')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.CharField(source='get_thumbnail_url', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = ProjectDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'



