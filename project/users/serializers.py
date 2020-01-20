from rest_framework import serializers
from users.models import MainUser
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_superuser')
        read_only_fields = ('id',)
        write_only_fields = ('password', 'first_name', 'last_name',)

    def create(self, validated_data):
        with transaction.atomic():
            user = MainUser.objects.create_user(**validated_data)
            user.save()
            return user
