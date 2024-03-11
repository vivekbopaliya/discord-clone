from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Message


class ChannelChatConsumer (AsyncWebsocketConsumer):
    async def connect(self):
        print('this is connected!')
        self.channel = self.scope['url_route']['kwargs']['channel_name']
        self.chanel_group_name = 'channel_%s' % self.channel

        await self.channel_layer.group_add(
            self.chanel_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        print('this is disconnected')
        await self.channel_layer.group_discard(
            self.chanel_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        channel = text_data_json['channel']

        Message.objects.create(
            username=username, channel=channel, message=message)

        await self.channel_layer.group_send(
            self.chanel_group_name,
            {
                'type': 'channel_message',
                'channel': channel,
                'message': message,
                'username': username,
            }
        )

    async def channel_message(self, event):
        message = event['message']
        username = event['username']
        channel = event['channel']

        await self.send(text_data=json.dumps({
            'channel': channel,
            'message': message,
            'username': username
        }))


class DirectChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.direct_message = self.scope['url_route']['kwargs']['sender']
        self.direct_message_name = 'sender_%s' % self.direct_message

        await self.channel_layer.on_group(
            self.direct_message_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.direct_message_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_json_data = json.loads(text_data)
        message = text_json_data['message']
        username = text_json_data['username']
        sender = text_json_data['sender']

        await self.channel_layer.on_add(
            self.chanel_group_name,
            {
                'type': 'direct_message',
                'message': message,
                'username': username,
                'sender': sender
            }
        )

    async def direct_message(self, event):
        message = event['message']
        username = event['username']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'sender': sender
        }))
