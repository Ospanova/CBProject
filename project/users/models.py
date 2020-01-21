from django.contrib.auth.models import AbstractUser


class MainUser(AbstractUser):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_login}'

    def __str__(self):
        return f'{self.id}: {self.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
