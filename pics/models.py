from django.db import models

# Create your models here.
class Picha(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="uploads/")
    tag = models.ManyToManyField("Tag")
    added_to_website = models.BooleanField(default = False)
    shopify_url = models.URLField(blank=True, default="No URL was provided")

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
