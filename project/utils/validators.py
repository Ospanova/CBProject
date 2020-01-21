from django.core.exceptions import ValidationError


def validate_rating(rating):
    if rating not in range(1, 6):
        raise ValidationError('Rating is not correct')
    return rating
