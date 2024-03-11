from django.contrib import admin
from .models import User, Channel, Server, Message, DirectMessge, Member
# Register your models here.
admin.site.register(User)
admin.site.register(Channel)
admin.site.register(Server)
admin.site.register(Message)
admin.site.register(DirectMessge)
admin.site.register(Member)
