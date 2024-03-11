from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Channel, Message, DirectMessge, Server, Member
from .serializers import MessageSerializer, DirectMessageSerializer, ServerSerializer, MemberSerializer, ChanbelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        response = Response()
        response.set_cookie('refresh_token', token)

        # token['name'] = user.name
        # token['id'] = user.id

        user.refreshToken = str(token)
        user.save()
        print(user)

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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

    if not request.user.id:
        return Response({'msg': 'Unauthorized'}, status=401)

    serializer = ServerSerializer(data=request.data)
    if serializer.is_valid():

        new_server = Server.objects.create(
            owner=request.user.id, name=serializer.data.get('name'))
        new_server.save()
        serialized_server = ServerSerializer(new_server, many=True).data

        return Response({'msg': 'success', 'data': serialized_server})
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

        user_id = request.user.id
        members = Member.objects.filter(id=user_id)
        servers = Server.objects.filter(id=members.get('server'))

        serializered_servers = ServerSerializer(servers)
        return Response({'msg': 'success'}, data=serializered_servers, status=200)
    except:
        return Response({'msg': 'Something went wrong on server, please try again'}, status=500)


@api_view(['GET'])
def fetch_members(request, server_id):
    try:
        if not request.user:
            return Response({'msg': 'Unauthorized'}, status=401)

        currentuser = Member.objects.filter(
            id=request.user.id, server=server_id)

        if currentuser.get('role') == 'GUEST':
            return Response({'msg': 'Guest cannot have access to server members'}, status=401)

        members = Member.objects.filter(server=server_id)

        serializerzed_members = MemberSerializer(members).data

        return Response({'msg': 'success'}, data=serializerzed_members, status=200)
    except:
        return Response({'msg': 'Something went wrong on server, please try again'}, status=500)
