from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    price = models.FloatField()
    description = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

