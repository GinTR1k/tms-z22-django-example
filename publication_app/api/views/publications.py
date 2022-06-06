from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from ..serializers.publications import PostSerializer
from ...models import Post


# CRUD
# GET, POST, PUT, PATCH, DELETE

class PostsViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'id']
