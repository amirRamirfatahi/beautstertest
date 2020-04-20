from rest_framework import serializers
from django.contrib.auth import get_user_model


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model()(
            email = validated_data.get('email'),
            username = validated_data.get('username')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

