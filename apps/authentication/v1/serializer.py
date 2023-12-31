from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.authentication.authen_core.utils import JwtTokenGenerator

User = get_user_model()


class JWTLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64, required=True)
    password = serializers.CharField(max_length=64, required=True, help_text='Leave empty if no change needed',
                                     style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            raise serializers.ValidationError(
                'password and username field required')

        user = authenticate(username=username, password=password)
        # if not user:
        #     raise CustomAPIException(ErrorMessage.LOGIN_FAIL)

        token_generator = JwtTokenGenerator()
        token = token_generator.get_token(user)
        user.sid = token_generator.jti
        return {
            'user': user,
            'token': token
        }


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

