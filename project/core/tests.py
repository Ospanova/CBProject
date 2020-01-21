from django.test import TestCase
from core.models import Review, Company
from users.models import MainUser


class ReviewTestCase(TestCase):
    def setUp(self):
        user = MainUser.objects.create(username='test', password='uljanek06')
        company = Company.objects.create(name='1fit', company_id='111')
        Review.objects.create(ip_address='1199',
                              rating=3,
                              title='Test',
                              summary='test',
                              reviewer=user,
                              company=company)

    def test_create(self):
        user = MainUser.objects.create(username='test2', password='uljanek06')
        company = Company.objects.create(name='1fit', company_id='111')
        review = Review.objects.create(ip_address='1199',
                                       rating=3,
                                       title='Test',
                                       summary='test',
                                       reviewer=user,
                                       company=company)
        return self.assertTrue(review.id == 2)

    def test_update(self):
        review = Review.objects.get(id=1)
        review.rating = 5
        return self.assertTrue(review.rating == 5)

    def test_delete(self):
        review = Review.objects.get(id=1)
        review.delete()
        return self.assertTrue(review.id is None)
