import os
from PIL import Image, ImageOps

from django.db import models
from django.conf import settings

# Create your models here.

class input1(models.Model):
    input_file = models.ImageField(upload_to = 'media/input1/', blank=True, null=True)
    #name = models.CharField(max_length=50)