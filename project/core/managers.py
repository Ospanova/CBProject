from django.db import models


class ReviewManager(models.Manager):

    def created_by_user(self, user):
        if (user.is_superuser):
            return super().all()
        return super().filter(reviewer=user)

    def get(self, id):
        return super().get(id == id)
