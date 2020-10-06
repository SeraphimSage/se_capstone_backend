from django.contrib import admin

from capstone_backend_app.models import MyUser, SavedAsteroid, Comment
# Register your models here.

admin.site.register(MyUser)
admin.site.register(SavedAsteroid)
admin.site.register(Comment)
