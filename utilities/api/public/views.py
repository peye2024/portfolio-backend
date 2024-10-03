from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .serializers import MaintainSerializer, ContactSerializer
from ...models import Maintainer, ContactMessage


class MaintainerListView(GenericViewSet, mixins.ListModelMixin):
    queryset = Maintainer.objects.all()
    serializer_class = MaintainSerializer
    permission_classes = (AllowAny,)


class ContactMessageCreateView(GenericViewSet, mixins.CreateModelMixin):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)
