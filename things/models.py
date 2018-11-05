from django.db import models
from django.urls import reverse


class Thing(models.Model):
    name = models.CharField(max_length=255)


class PrivateThing(models.Model):
    name = models.CharField(max_length=255)
