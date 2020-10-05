from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class MyUser(AbstractUser):
    username = models.EmailField(max_length=254)
    display_name = models.CharField(max_length=80, blank=False, null=False)


class SavedAsteroid(models.Model):
    name = models.CharField(max_length=240)
    favorite = models.BooleanField(default=False)
    date_saved = models.DateTimeField(default=timezone.now)
    note = models.TextField()
