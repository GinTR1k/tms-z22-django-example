from rest_framework import routers

from .likes import LikeViewSet


api_router = routers.DefaultRouter()
api_router.register('likes', LikeViewSet)
