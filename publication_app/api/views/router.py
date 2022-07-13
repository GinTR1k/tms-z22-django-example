from rest_framework import routers

from .publications import PostsViewSet
from .users import UserViewSet

api_router = routers.DefaultRouter()
api_router.register('posts', PostsViewSet)
api_router.register('users', UserViewSet)
