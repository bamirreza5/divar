# Generated by Django 5.1.4 on 2024-12-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
