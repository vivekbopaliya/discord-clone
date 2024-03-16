from rest_framework.serializers import ModelSerializer
from .models import Message, DirectMessge, Server, Member, Channel, User
from rest_framework import serializers
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class DirectMessageSerializer(ModelSerializer):
    class Meta:
        model = DirectMessge
        fields = '__all__'


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = ['name']


class ResponeServerSerializer(ModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ChanbelSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name']


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "password2")
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }

    def save(self):
        user = get_user_model()(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Passwords do not match!"})

        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")
