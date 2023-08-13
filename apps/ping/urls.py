from django.urls import path

from apps.ping.views import ping

ping_urlpatterns = [
    path('ping', ping, name='ping'),
]
