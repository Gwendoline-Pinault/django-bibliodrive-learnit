# Generated by Django 5.1.2 on 2024-11-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
