# Generated by Django 5.0.3 on 2024-03-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0006_remove_picha_tag_picha_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picha',
            name='shopify_url',
            field=models.URLField(default='No URL was provided', null=True),
        ),
    ]
