# Generated by Django 4.0.1 on 2022-01-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]