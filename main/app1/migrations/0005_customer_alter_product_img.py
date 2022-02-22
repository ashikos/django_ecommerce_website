# Generated by Django 4.0.1 on 2022-01-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_product_desc_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='products'),
        ),
    ]