from rest_framework import serializers
from .models import Thing, PrivateThing


class ThingSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Thing
        fields = "__all__"


class PrivateThingSerialzer(serializers.ModelSerializer):

    class Meta:
        model = PrivateThing
        fields = "__all__"
