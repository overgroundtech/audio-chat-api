from django.urls import path

from . import views

urlpatterns = [
    path('token', views.obtain_token, name='token'),
]
