from rest_framework.routers import DefaultRouter
from .views import SocialPostViewSet

router = DefaultRouter()
router.register(r'social-posts', SocialPostViewSet, basename='social-posts')

urlpatterns = router.urls
