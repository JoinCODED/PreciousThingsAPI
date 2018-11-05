from rest_framework import serializers
from .models import Thing, PrivateThing


class ThingSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Thing
        exclude = ('created',)


class PrivateThingSerialzer(serializers.ModelSerializer):

    class Meta:
        model = PrivateThing
        exclude = ('created',)
