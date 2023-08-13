from django_filters.rest_framework import DjangoFilterBackend
from apps.users.user_repository import UserRepository
from apps.users.v1.filters import UserFilter
from apps.users.v1.serializer import UserSerializer
from core.base_model_view_set import BaseModelViewSet


class UserApiView(BaseModelViewSet):
    authentication_classes = []
    serializer_class = UserSerializer
    repository_class = UserRepository
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter