from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model


class VerifyotpSerializer(serializers.ModelSerializer):
    redirect_url = serializers.CharField(required=False, default='/')

    class Meta:
        model = get_user_model()
        fields = ('username', 'otp', 'token', 'redirect_url')
        extra_kwargs = {
            'otp': {'write_only': True},
            'token': {'read_only': True}
        }

    def validate_otp(self, value):
        if not self.instance.otp == value:
            raise exceptions.ValidationError(detail='Incorrect OTP',
                                             code='invalid')
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        data.update({
            'redirect_url': self.validated_data.get('redirect_url')
        })
        return data

    def update(self, instance, validated_data):
        instance.set_token()
        return instance
