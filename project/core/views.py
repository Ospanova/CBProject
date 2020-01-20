from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
from core.models import Review
from core.serializers import BaseReviewSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import HasPermission
from rest_framework.views import APIView

class ReviewListViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = BaseReviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Review.reviews.created_by_user(self.request.user)

class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (HasPermission,)
    serializer_class = BaseReviewSerializer

    def get_queryset(self):
        return Review.reviews.created_by_user(self.request.user)

    def perform_create(self, serializer):
        return serializer.save(reviewer=self.request.user)