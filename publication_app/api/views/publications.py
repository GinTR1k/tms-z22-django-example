from rest_framework import filters
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.publications import PostSerializer
from ...models import Post


# CRUD
# GET, POST, PUT, PATCH, DELETE

class PostsView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'id']


"""
Домашнее задание до понедельника (дополнительно к прошлой):
1. API интерфейс для получения всех публикаций
2. API интерфейс для получения всех тэгов
3. *API интерфейс для получения всех постов определенного тэга
4. Сделать пагинацию для всех методов, которые выводят список объектов
"""
