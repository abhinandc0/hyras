from django.db import models

# Models for Products

class Product(models.Model):
    LIVE = 1
    DELETE=0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    priority = models.IntegerField()
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self) -> str:
        return self.name