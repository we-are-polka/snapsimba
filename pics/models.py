from django.db import models

# Create your models here.
class Picha(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="uploads/flowers")
    edited_image = models.ImageField(upload_to="uploads/edited_images", blank=True)
    tag = models.ManyToManyField("Tag")
    flower_type = models.ManyToManyField("FlowerType", blank=False, default='no_flower_type')
    collection = models.ManyToManyField("Collection",  blank=False, default='no_collection')
    shopify_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class FlowerType(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to="uploads/flower_types")

    def __str__(self):
        return self.name
    
class Collection(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to="uploads/collections")
    
    def __str__(self):
        return self.name
