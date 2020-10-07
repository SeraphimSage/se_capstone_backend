from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from capstone_backend_app.models import MyUser, SavedAsteroid, Comment
from capstone_backend_app.serializers import MyUserSerializer, SavedAsteroidSerializer, CommentSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class SavedAsteroidViewSet(viewsets.ModelViewSet):
    queryset = SavedAsteroid.objects.all()
    serializer_class = SavedAsteroidSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
