from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.tags import TagDetailSerializer, TagSerializer
from ...models import Tag


class TagViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    action_serializers = {'retrieve': TagDetailSerializer}
    lookup_field = 'name'

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)
