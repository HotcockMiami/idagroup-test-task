from django.db import models
from django.utils import timezone

# Тут ничего необычного, храним оригинал, копию измененного размера, URL и дату создания

class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.URLField()
    image_orig = models.ImageField(null=True, blank=True, upload_to='images_orig/')
    image_resized = models.ImageField(null=True, blank=True, upload_to='images_resized/')
    created_at = models.DateTimeField(default=timezone.now)
