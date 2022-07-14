from django.db import models

# Create your models here.
class Vegetables(models.Model):
    product = models.CharField(max_length=250)
    category = models.PositiveIntegerField(default=2)
