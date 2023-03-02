from rest_framework import routers
from . views import BlogViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'posts/', BlogViewSet, 'blogs')
router.register(r'users/', UserViewSet, 'users')

urlpatterns = router.urls

