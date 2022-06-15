from django.db import models

# Create your models here.

class name(models.Model):
    boyname = models.CharField(max_length=50)
    girlname = models.CharField(max_length=50)
  