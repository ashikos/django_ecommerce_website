# Generated by Django 4.0.1 on 2022-02-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_checkout_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
