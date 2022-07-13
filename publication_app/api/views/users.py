from django.contrib.auth.models import User
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from ..serializers.users import UserSerializer


class UserViewSet(GenericViewSet, RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
