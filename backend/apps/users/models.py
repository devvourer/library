from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from random import randint


class User(AbstractUser):
    activation_code = models.CharField(max_length=6, blank=True, null=True, verbose_name='activation code')
    verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    def generate_activation_code(self):
        self.activation_code = str(randint(100000, 999999))
        self.save()


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.user.username
