from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

from .models import Thing, PrivateThing


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'token']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data


class ThingSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Thing
        fields = "__all__"


class PrivateThingSerialzer(serializers.ModelSerializer):

    class Meta:
        model = PrivateThing
        fields = "__all__"
