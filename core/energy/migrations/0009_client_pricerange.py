# Generated by Django 3.1.2 on 2020-10-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0008_auto_20201026_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='priceRange',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
