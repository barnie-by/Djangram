# Generated by Django 4.0.2 on 2022-03-16 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_core', '0007_remove_posts_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='uniqueid',
        ),
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
