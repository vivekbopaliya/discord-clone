from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path('auth/register/', views.registerView),
    path('auth/login/', views.loginView),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/user/', views.user),



    path('channel/<str:channel_name>/',  views.fetch_messages_by_channel_name,
         name='channel_message'),
    path('direct/<str:sender>/',
         views.fetch_messages_by_username, name='direct_message'),
    path('server/create/', views.create_server, name='create_server'),
    path('server/join/', views.join_server, name='join_server'),
    path('server/getServers/', views.fetch_servers_by_userid,
         name='get_servers_by_userid'),
    path('members/getMembers/<str:server_id>/',
         views.fetch_members, name='get_members'),

    path('channel/get/<str:server_id>/',
         views.get_channels, name='get_channels'),
    path('channel/create/<str:server_id>/',
         views.create_channel, name='create_channel')
]
