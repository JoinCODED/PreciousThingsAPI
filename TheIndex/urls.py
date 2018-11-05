"""TheIndex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

from things import views


class OptionalSlashRouter(routers.DefaultRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(routers.DefaultRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'things', views.ThingViewSet)
router.register(r'private-things', views.PrivateThingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', obtain_jwt_token),
    path('signup/', views.UserCreateAPIView.as_view())
]
