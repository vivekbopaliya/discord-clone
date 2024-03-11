from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(models.Model):
    name = models.CharField(blank=False, null=False)
    avatar = models.ImageField(blank=True, upload_to='avatar/')
    refreshToken = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Server(TimeStampedModel):
    name = models.CharField(blank=False, null=False)
    profile = models.ImageField(blank=True, upload_to='serverAvatar/')
    owner = models.ForeignKey(
        User, related_name='server_owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Channel(TimeStampedModel):
    name = models.CharField(blank=False, null=False)
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Member (TimeStampedModel):
    username = models.ForeignKey(
        User, related_name='member', on_delete=models.CASCADE)
    server = models.ForeignKey(
        Server, related_name='server_member', on_delete=models.CASCADE)
    role_choices = (
        ('ADMIN', 'Admin'),
        ('MODERATOR', 'Moderator'),
        ('GUEST', 'Guest')
    )
    role = models.CharField(
        max_length=20, choices=role_choices, default='GUEST')


class Message(TimeStampedModel):
    username = models.ForeignKey(
        Member, related_name='message_sender', on_delete=models.CASCADE)
    channel = models.ForeignKey(
        Channel, related_name='channel_message', on_delete=models.CASCADE)
    message = models.CharField(null=False, blank=False, max_length=100)
    is_deleted = models.BooleanField(default=False)
    is_updated = models.BooleanField(default=False)


class DirectMessge(TimeStampedModel):
    username = models.ForeignKey(
        User, related_name='username', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, related_name='sender', on_delete=models.CASCADE)
    message = models.CharField(null=False, blank=False, max_length=100)
    is_deleted = models.BooleanField(default=False)
    is_updated = models.BooleanField(default=False)
