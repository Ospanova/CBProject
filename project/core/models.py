from django.db import models
from users.models import MainUser
from core.managers import ReviewManager
# Create your models here.

MAX_SIZE_SUMMARY = 10000;

class Company (models.Model):
    name = models.CharField(max_length=64)
    company_id = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.name} : {self.company_id}'

class Review (models.Model):
    rating = models.IntegerField(default=1)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=MAX_SIZE_SUMMARY)
    ip_address = models.CharField(max_length=24, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='reviews')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_reviews')
    reviews = ReviewManager()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.reviewer}: {self.title}'

