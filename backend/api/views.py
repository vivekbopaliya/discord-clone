from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Channel, Message, DirectMessge, Server, Member, User
from .serializers import MessageSerializer, DirectMessageSerializer, ServerSerializer, MemberSerializer, ChanbelSerializer, UserSerializer, RegistrationSerializer, LoginSerializer, AccountSerializer, ResponeServerSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import exceptions as rest_exceptions, response, decorators as rest_decorators, permissions as rest_permissions
from rest_framework_simplejwt import tokens, views as jwt_views, serializers as jwt_serializers, exceptions as jwt_exceptions
from django.views.decorators.csrf import csrf_protect


def get_user_tokens(email):
    user = User.objects.get(email=email)
    refresh = RefreshToken.for_user(user)

    return {
        "refresh_token": str(refresh),
        "access_token": str(refresh.access_token),
    }


@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([])
def registerView(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    if user is not None:
        return Response(status=200)
    return Response({'msg': 'invalid data'}, )


@api_view(["POST"])
def loginView(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        tokens = get_user_tokens(email)

        response_data = {
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
        }
        return Response(data=response_data, status=200)

    else:
        return Response({'msg': 'Invalid data'}, status=401)


@api_view(['GET'])
def fetch_messages_by_channel_name(request, channel_name):
    try:
        # messages = Message.objects.select_related(
        #     'channel').filter(channel__name=channel_name)
        channel = Channel.objects.get(id=channel_name)
        messages = Message.objects.filter(channel=channel)
        serialized_messages = MessageSerializer(messages, many=True).data
        return Response({'messages': serialized_messages})
    except Channel.DoesNotExist:
        return Response({'error': 'Channel does not exist'}, status=404)


@api_view(['POST'])
def create_server(request):

    if not request.user:
        return Response({'msg': 'Unauthorized'}, status=401)

    serializer = ServerSerializer(data=request.data)
    if serializer.is_valid():

        new_server = Server.objects.create(
            owner=request.user, name=serializer.data.get('name'), members=request.user)
        new_server.save()

        member = Member.objects.create(
            username=request.user, server=new_server, role='ADMIN')
        member.save()

        return Response({'msg': 'Done'}, status=200)
    else:
        return Response({'msg': 'Invalid data'},  status=400)


def join_server(request):
    serializers = MemberSerializer(data=request.data)

    if serializers.is_valid():
        server = Server.objects.get(id=serializers.validated_data.get('id'))
        member = Member.objects.create(
            server=server.id, username=request.user.name)

        member.save()
        serialized_member = MemberSerializer(member).data
        return Response({'msg': "success", "data": serialized_member['id']}, status=200)
    else:
        return Response({'msg': 'Invalid data!', 'error': serializers.errors}, status=400)


def create_channel(request, server_id):
    serializers = ChanbelSerializer(data=request.data)

    if serializers.is_valid():
        server = Server.objects.get(id=server_id)
        members = Member.objects.filter(
            server=server.get('id'), username=request.user.name)

        serilaized_member = MemberSerializer(members)

        if serilaized_member['role'] == 'GUEST':
            raise serializers.ValidationError(
                'You need to be owner or moderator of server to do this!')

        channel = Channel.objects.create(
            server=server_id, name=request.data.name)
        channel.save()
        return Response({'msg': 'success', 'data': channel.id}, status=200)


@api_view(['GET'])
def fetch_messages_by_username(request, sender):
    try:
        username = request.user.name
        message = DirectMessge.objects.filter(
            sender=sender, username=username)
        serialized_messages = DirectMessageSerializer(message, many=True)
        return Response({'messages': serialized_messages}, status=200)
    except any:
        return Response({'msg': 'Something went wrong on server, please try again'}, status=500)


@api_view(['GET'])
def fetch_servers_by_userid(request):
    try:

        if not request.user:
            return Response({'msg': 'Unauthorized'}, status=401)

        member = Member.objects.filter(username=request.user)
        # Fetching servers associated with the member
        servers = Server.objects.filter(members=request.user)

        serialized_servers = ResponeServerSerializer(
            servers, many=True)
        return Response({'servers': serialized_servers.data}, status=200)
    except Exception as e:
        return Response({'msg': e}, status=500)


@api_view(['GET'])
def fetch_members(request, server_id):
    try:
        if not request.user:
            return Response({'msg': 'Unauthorized'}, status=401)
        members = Member.objects.filter(server=server_id)
        print(members)
        serialized_memebers = MemberSerializer(members, many=True)

        return Response({'members': serialized_memebers.data}, status=200)
    except:
        return Response({'msg': 'Something went w   rong on server, please try again'}, status=500)


@rest_decorators.api_view(["GET"])
def user(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return response.Response(status_code=404)

    serializer = AccountSerializer(user)
    return response.Response(serializer.data)
