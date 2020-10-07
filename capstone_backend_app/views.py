from django.shortcuts import render

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from capstone_backend_app.models import MyUser, SavedAsteroid, Comment
from capstone_backend_app.serializers import MyUserSerializer, MyUserSerializerWithToken, SavedAsteroidSerializer, CommentSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def post(self, request, format=None):
        serializer = MyUserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['post'])
    # def createUser(self, request, pk=None):
    #     serializer = MyUserSerializerWithToken(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavedAsteroidViewSet(viewsets.ModelViewSet):
    queryset = SavedAsteroid.objects.all()
    serializer_class = SavedAsteroidSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
