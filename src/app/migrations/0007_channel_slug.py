# Generated by Django 4.0.1 on 2022-01-27 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_channel_remove_video_user_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]