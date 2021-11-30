from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Product(models.Model):
    make = models.TextField(null=True)
    car_model = models.TextField(null=True)
    price = models.FloatField(null=True)
    engine = models.TextField(null=True)
    fuel = models.TextField(null=True)
    body_type = models.TextField(null=True)
    colour = models.TextField(null=True)
    url = models.TextField(null=True)
    image = models.URLField(null=True)

class Recommendation(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='recommendation'
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='saved_recommendation_owner'
    )



