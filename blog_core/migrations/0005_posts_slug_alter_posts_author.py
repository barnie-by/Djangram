# Generated by Django 4.0.2 on 2022-03-02 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_core', '0004_delete_media_alter_likes_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]