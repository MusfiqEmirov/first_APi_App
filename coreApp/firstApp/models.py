from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=60)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)

    def save(self, *args,**kargs):
        self.slug = slugify(self.name)
        super().save(*args,**kargs) 

    def __str__(self):
        return self.name
    
