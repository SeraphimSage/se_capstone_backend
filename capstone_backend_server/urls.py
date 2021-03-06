"""capstone_backend_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from capstone_backend_app import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user/')
router.register(r'savedasteroid', views.SavedAsteroidViewSet,
                basename='savedasteroid/')
router.register(r'comment', views.CommentViewSet, basename='comment/')

urlpatterns = [
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh/', refresh_jwt_token),
    path('auth/verify/', verify_jwt_token),
    path('api/', include(router.urls)),
    path('users/', views.UserList.as_view()),
    path('admin/', admin.site.urls),
]
