from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="covers/", )
    price = models.FloatField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

