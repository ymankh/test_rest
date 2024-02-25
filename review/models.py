from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    text = models.CharField(max_length=500)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


