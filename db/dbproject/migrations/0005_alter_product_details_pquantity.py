# Generated by Django 5.0 on 2024-01-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbproject', '0004_alter_product_details_pquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='pquantity',
            field=models.IntegerField(max_length=3),
        ),
    ]