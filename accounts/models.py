from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings


# Create your models here.



class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')