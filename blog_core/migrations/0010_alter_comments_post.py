# Generated by Django 4.0.2 on 2022-03-28 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_core', '0009_alter_comments_author_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog_core.posts'),
        ),
    ]
