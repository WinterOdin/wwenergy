# Generated by Django 3.1.2 on 2020-10-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0009_client_pricerange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='priceRange',
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]