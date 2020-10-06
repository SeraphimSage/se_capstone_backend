from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from capstone_backend_app.models import MyUser, SavedAsteroid, Comment
from capstone_backend_app.serializers import MyUserSerializer, SavedAsteroidSerializer, CommentSerializer

# Create your views here.
