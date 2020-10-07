from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

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

# found instructions for tokens from https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a


class MyUserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = MyUser
        fields = ('token', 'username', 'password')


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
