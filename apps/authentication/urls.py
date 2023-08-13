from rest_framework import routers

from apps.authentication.v1.views import JWTAuthAPIView

router = routers.DefaultRouter()
router.register('v1/auth', JWTAuthAPIView, basename='auth')
urlpatterns = router.urls
