from rest_framework import serializers
from core.models import Review, Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('company_id', 'name',)
        read_only_fields = ('id')

class BaseReviewSerializer(serializers.ModelSerializer):
    company = CompanySerializer

    class Meta:
        model = Review
        fields = ('id', 'rating', 'title', 'summary', 'ip_address', 'created_at', 'reviewer', 'company', )
        read_only_fields = ('id', 'created_at', 'reviewer',)

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Rating is not correct')
        return rating