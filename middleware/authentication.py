from django.core.cache import cache
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuth(TokenAuthentication):
    def get_model(self):
        return get_user_model()

    def authenticate_credentials(self, key):
        model = self.get_model()

        cached_user_id = cache.get(key)
        if cached_user_id:
            user = model(id=cached_user_id)
            return user, key


        user = model.objects.filter(token=key).first()

        if not user:
            raise exceptions.AuthenticationFailed('Invalid token.')

        return user, key
