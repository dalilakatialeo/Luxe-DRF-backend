from django.db import models

# Create your models here.
class Product(models.Model):
    make = models.TextField(null=True)
    model = models.TextField(null=True)
    price = models.FloatField(null=True)
    engine = models.TextField(null=True)
    fuel = models.TextField(null=True)
    body_type = models.TextField(null=True)
    colour = models.TextField(null=True)
    url = models.TextField(null=True)
    image = models.URLField(null=True)



