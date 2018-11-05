from django.contrib import admin

from .models import Thing, PrivateThing


admin.site.register(Thing)
admin.site.register(PrivateThing)
