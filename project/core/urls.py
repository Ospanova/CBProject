from rest_framework.routers import DefaultRouter
from core.views import ReviewListViewSet, ReviewViewSet

urlpatterns = []
router = DefaultRouter()
router.register('reviews', ReviewListViewSet, base_name='reviews')
router.register('review', ReviewViewSet, base_name='reviews')
urlpatterns += router.urls
