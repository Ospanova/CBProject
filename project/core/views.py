from rest_framework import viewsets, mixins
from core.models import Review
from core.serializers import BaseReviewSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import HasPermission


class ReviewListViewSet(viewsets.ReadOnlyModelViewSet):
    """
        Viewset for getting reviews for user and admin
    """

    serializer_class = BaseReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Review.reviews.created_by_user(self.request.user)


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """
        ViewSet for deleting, updating and creating reviews
    """

    permission_classes = (HasPermission,)
    serializer_class = BaseReviewSerializer

    def get_queryset(self):
        return Review.reviews.created_by_user(self.request.user)

    def perform_create(self, serializer):
        return serializer.save(reviewer=self.request.user,
                               ip_address=self.request.META.get('REMOTE_ADDR'))
