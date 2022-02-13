# Generated by Django 4.0.1 on 2022-01-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_channel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]