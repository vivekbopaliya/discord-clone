from django.urls import re_path
from .consumers import ChannelChatConsumer, DirectChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/channel/(?P<room_name>\w+)/$',
            ChannelChatConsumer.as_asgi()),

    re_path(r'ws/chat/(?P<sender>\w+)/$', DirectChatConsumer.as_asgi())

]
