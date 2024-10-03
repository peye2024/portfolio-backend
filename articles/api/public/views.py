from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from ...models import Article
from .serializers import (
ArticleSerializer
)

class ArticleListView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'
