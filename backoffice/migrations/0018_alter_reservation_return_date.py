# Generated by Django 5.1.2 on 2024-12-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0017_rename_reserve_title_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
