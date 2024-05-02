from django.contrib import admin
from .models import Picha, Tag, FlowerType, Collection

# Register your models here.
@admin.register(Picha)
class PichaAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'tag', 'flower_type', 'collection', 'shopify_url')

admin.site.register(Tag)
admin.site.register(FlowerType)
admin.site.register(Collection)