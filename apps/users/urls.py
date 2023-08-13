from rest_framework import routers

from apps.users.v1.views import UserApiView

router = routers.DefaultRouter()
router.register('v1/users', UserApiView, basename='user')
urlpatterns = router.urls
