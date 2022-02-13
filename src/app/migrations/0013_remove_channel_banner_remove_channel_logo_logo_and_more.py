# Generated by Django 4.0.1 on 2022-02-04 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_watch_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='logo',
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.channel')),
            ],
        ),
    ]
