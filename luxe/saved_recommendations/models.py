from django.db import models
from django.contrib.auth import get_user_model, 

# Create your models here.

class SavedRecommendations(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_recommendations')
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='product_recommendations'
    )
    