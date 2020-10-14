from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class MyUser(AbstractUser):
    username = models.EmailField(max_length=254, unique=True)
    display_name = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.username


class SavedAsteroid(models.Model):
    name = models.CharField(max_length=240)
    saved_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False, blank=True)
    date_saved = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.saved_by}"


class Comment(models.Model):
    title = models.CharField(max_length=240)
    attatched = models.ForeignKey(SavedAsteroid, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    @property
    def rating(self):
        return self.up_vote - self.down_vote

    def __str__(self):
        return self.title
