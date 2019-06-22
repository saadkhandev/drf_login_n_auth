from rest_framework import routers
from rental import views
from django.urls import path, include
from django.contrib import admin
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken'))
]
