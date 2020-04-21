from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if not self.instance.check_password(value):
            raise exceptions.ValidationError(detail='Incorrect Password',
                                             code='invalid')
        return value

    def update(self, instance, validated_data):
        instance.set_otp()
        return instance
