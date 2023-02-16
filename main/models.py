from django.db import models
from django.contrib.auth.models import AnonymousUser


class Item(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)


class Order(models.Model):

    items = models.ManyToManyField(Item)
