# Generated by Django 4.0.1 on 2022-02-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_channel_banner_remove_channel_logo_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]