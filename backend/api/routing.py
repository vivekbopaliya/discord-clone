from django.urls import re_path
from .consumers import ChannelChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<channel_name>\w+)/$', ChannelChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<sender>\w+)/$', ChannelChatConsumer.as_asgi())

]
