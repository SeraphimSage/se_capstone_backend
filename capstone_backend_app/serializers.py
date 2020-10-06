from rest_framework import serializers

from capstone_backend_app.models import MyUser, SavedAsteroid, Comment


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'id',
            'username',
            'password',
            'display_name'
        ]


class SavedAsteroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedAsteroid
        fields = [
            'id',
            'name',
            'saved_by',
            'favorite',
            'date_saved',
            'note'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'title',
            'up_vote',
            'down_vote',
            'post_date',
            'rating'
        ]
