import os
from PIL import Image, ImageOps

from django.db import models
from django.conf import settings

# Create your models here.

class input(models.Model):
    input_file = models.ImageField(upload_to = 'media/input1/')
    #name = models.CharField(max_length=50)