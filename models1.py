from django.db import models
from django.contrib.auth.models import User




class Categories(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Items(models.Model):
    subcategory = models.ForeignKey(SubCategories, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=100)

class Ratings(models.Model):
    item = models.ForeignKey(Items, on_delete=models.PROTECT)
    by = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.IntegerField(min_value = 1, max_value = 5)


