import jwt
from rest_framework import authentication, exceptions
from profiles.models import User


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if auth_data == b'':
            raise exceptions.AuthenticationFailed('Please provide the token,login')

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, 'secret')
            # print(payload)
            try:
                user = User.objects.get(user_id=payload['user'])
                return (user, token)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')
