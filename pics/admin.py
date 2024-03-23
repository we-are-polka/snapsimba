from django.contrib import admin
from .models import Picha, Tag

# Register your models here.
@admin.register(Picha)
class PichaAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'tag', 'added_to_website', 'shopify_url')

admin.site.register(Tag)