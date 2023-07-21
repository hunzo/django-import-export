from django.db import models
from django.core.exceptions import ValidationError

def validate_digit_length(code):
    if not (code.isdigit() and len(code) == 10):
        raise ValidationError(f'{code} must be 10 digit', params={'code': code})

class CodeModels(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(
        verbose_name="Code",
        max_length=10,
        validators=[validate_digit_length],
        default="0123456789"
    )
