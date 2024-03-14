from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):

        if not email:
            raise ValueError("Email is required")

        if not username:
            raise ValueError("Username is required")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password, **kwargs):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return


class User(AbstractBaseUser):
    email = models.EmailField(null=False, blank=False,
                              unique=False, default='abc@gmail.com')
    username = models.CharField(
        max_length=50, blank=False, null=False, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


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
        User, related_name='name', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, related_name='sender', on_delete=models.CASCADE)
    message = models.CharField(null=False, blank=False, max_length=100)
    is_deleted = models.BooleanField(default=False)
    is_updated = models.BooleanField(default=False)
