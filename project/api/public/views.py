from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from coreapp.pagination import LargeResultsSetPagination
from ...models import Tag, Project
from .serializers import (
    TagSerializer, ProjectSerializer
)


class TagListView(GenericViewSet, mixins.ListModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


class ProjectListView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'
    pagination_class = LargeResultsSetPagination


