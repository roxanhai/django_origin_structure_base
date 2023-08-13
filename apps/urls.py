from django.urls import include, path

from apps.ping.urls import ping_urlpatterns

urlpatterns = [
    path('', include('apps.authentication.urls')),
    path('', include('apps.users.urls')),
    path('', include(ping_urlpatterns))
]
