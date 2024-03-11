from rest_framework.serializers import ModelSerializer
from .models import Message, DirectMessge, Server, Member, Channel
from rest_framework import serializers


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
        fields = '__all__'


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ChanbelSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
