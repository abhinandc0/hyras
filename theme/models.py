from django.db import models

# Create your models here.
class SiteTheme(models.Model):
    banner = models.ImageField(upload_to='media/banner/')
    caption = models.TextField()