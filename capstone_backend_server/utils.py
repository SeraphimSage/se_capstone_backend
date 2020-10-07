from capstone_backend_app.serializers import MyUserSerializer


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': MyUserSerializer(user, context={'request': request}).data
    }
