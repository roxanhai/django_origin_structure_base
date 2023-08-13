from django.contrib.auth import get_user_model

from core.base_repository import (RepositoryBase)

User = get_user_model()


class UserRepository(RepositoryBase):
    class Meta:
        model = User
