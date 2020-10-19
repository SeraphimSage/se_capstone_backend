from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters, generics

from capstone_backend_app.models import MyUser, SavedAsteroid, Comment
from capstone_backend_app.serializers import MyUserSerializer, MyUserSerializerWithToken, SavedAsteroidSerializer, CommentSerializer

# Create your views here.

@api_view(["GET"])
def test_500(request):
    raise (Exception("I AM GOING TO TRIGGER A 500"))

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    # def get(self, request, format=None):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def post(self, request, format=None):
        serializer = MyUserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    def get(self, request, format=None):
        users = MyUser.objects.all()
        serializer = MyUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MyUserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SavedAsteroidViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    # user = self.request.user
    queryset = SavedAsteroid.objects.all()
    serializer_class = SavedAsteroidSerializer
    # filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['saved_by']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
