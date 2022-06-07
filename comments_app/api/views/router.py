from rest_framework import routers

from .comments import CommentViewSet


api_router = routers.DefaultRouter()
api_router.register('comments', CommentViewSet)
