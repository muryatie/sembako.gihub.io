# Generated by Django 4.1.7 on 2023-02-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
