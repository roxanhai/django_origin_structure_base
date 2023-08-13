# Create your views here.
from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from apps.authentication.authen_core.signals import user_logout, user_login
from apps.authentication.v1.serializer import JWTLoginSerializer, UserAccountSerializer, \
    UserRegistrationSerializer
from apps.users.models import User
from core.base_model_view_set import BaseGenericViewSet


class JWTAuthAPIView(BaseGenericViewSet):
    serializer_action_classes = {
        'login': JWTLoginSerializer,
        'register': UserRegistrationSerializer
    }

    @action(methods=['post'], detail=False)
    def logout(self, request):
        response = Response(data=None)
        response.delete_cookie(api_settings.JWT_AUTH_COOKIE)
        user_logout.send(sender=request.user.__class__, user=request.user)
        return response

    @swagger_auto_schema(request_body=JWTLoginSerializer)
    @action(methods=['post'], detail=False, authentication_classes=[])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token = serializer.validated_data.get('token')

        data = {
            'token': token,
            'user': UserAccountSerializer(user).data
        }
        response = Response(data=data)
        if api_settings.JWT_AUTH_COOKIE:
            expiration = (datetime.utcnow() +
                          api_settings.JWT_EXPIRATION_DELTA)
            response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                token,
                                expires=expiration,
                                httponly=True)

        user_login.send(sender=request.user.__class__, user=user)
        return response


    @action(methods=['post'], detail=False, authentication_classes=[])
    def register_client(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User(**serializer.validated_data)
        user.set_password(user.password)
        user.save()
        return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)
