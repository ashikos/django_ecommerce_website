# Generated by Django 4.0.1 on 2022-01-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_customer_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
