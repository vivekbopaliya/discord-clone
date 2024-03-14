from django.urls import path
from . import views

urlpatterns = [

    path('auth/register/', views.registerView),
    path('auth/login/', views.loginView),
    path('auth/refresh-token/', views.CookieTokenRefreshView.as_view()),
    path('auth/logout/', views.logoutView),

    path('channel/<str:channel_name>/',  views.fetch_messages_by_channel_name,
         name='channel_message'),
    path('direct/<str:sender>/',
         views.fetch_messages_by_username, name='direct_message'),
    path('server/create/', views.create_server, name='create_server'),
    path('server/join/', views.join_server, name='join_server'),
    path('server/getServers/', views.fetch_servers_by_userid,
         name='get_servers_by_userid'),
    path('members/getMembers', views.fetch_members, name='get_members'),
]
