"""URL Configuration."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('token', include('api.urls')),
    path('admin/', admin.site.urls),
]
