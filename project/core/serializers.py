from rest_framework import serializers
from core.models import Review, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_id', 'name',)
        read_only_fields = ('id')


class BaseReviewSerializer(serializers.ModelSerializer):
    """
        Base serializer for review with validating rating
    """

    company = CompanySerializer

    class Meta:
        model = Review
        fields = ('id', 'rating', 'title', 'summary', 'ip_address',
                  'created_at', 'reviewer', 'company',)
        read_only_fields = ('id', 'created_at', 'reviewer', 'ip_address',)
