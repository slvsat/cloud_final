from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin, AbstractUser

class User(AbstractUser):
    pass
