from django.db import models

# Create your models here.
class image(models.Model):
    upload = models.ImageField()
    description = models.CharField(max_lenght=225, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'