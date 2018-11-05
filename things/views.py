import time

from rest_framework.generics import CreateAPIView
from rest_framework import viewsets, mixins, serializers, permissions

from .models import Thing, PrivateThing
from .serializers import ThingSerialzer, PrivateThingSerialzer, UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ThingViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows things to be viewed
    """
    queryset = Thing.objects.all()
    serializer_class = ThingSerialzer


class PrivateThingViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Private API endpoint that allows private things to be viewed
    """
    queryset = PrivateThing.objects.all()
    serializer_class = PrivateThingSerialzer
    permission_classes = [permissions.IsAuthenticated]
