# Generated by Django 5.0.3 on 2024-03-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0005_rename_status_picha_added_to_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picha',
            name='tag',
        ),
        migrations.AddField(
            model_name='picha',
            name='tag',
            field=models.ManyToManyField(to='pics.tag'),
        ),
    ]
