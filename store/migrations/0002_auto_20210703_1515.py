# Generated by Django 3.1 on 2021-07-03 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Images',
            field=models.ImageField(upload_to='photos/products'),
        ),
    ]
