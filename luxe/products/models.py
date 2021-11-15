from django.db import models

# Create your models here.
class Product(models.Model):
    make = models.TextField()
    model = models.TextField()
    price = models.FloatField()
    engine = models.TextField()
    colour = models.TextField()
    image = models.URLField()
    rating = models.FloatField()
    owner = models.CharField(max_length=200)
    # make_rating = models.TextField()
    # model_rating = models.TextField()
    # price_rating = models.FloatField()
    # engine_rating = models.TextField()
    # colour_rating = models.TextField()
    # image_rating = models.URLField()
    # rating_total = models.FloatField()
    # owner = models.CharField(max_length=200)

