from django.db import models

# Create your models here.
class image(models.Model):
    upload = models.ImageField()