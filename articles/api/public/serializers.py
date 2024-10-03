from rest_framework import serializers
from coreapp.models import Document
from project.api.public.serializers import TagSerializer
from ...models import Article


class ArticleDocumentSerializer(serializers.ModelSerializer):
    document_url = serializers.CharField(source='get_url', read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'document_url')



class ArticleSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.CharField(source='get_thumbnail_url', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = ArticleDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
