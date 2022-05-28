from uuid import uuid4

from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from users.models import CustomUser


class Posts(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    post_image = models.ImageField(null=True)

    def __str__(self) -> str:
        return f'Post {self.id}, by {self.author}, {self.slug}'

    def save(self, *args, **kwargs):
        value = uuid4()
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    liked_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'User likes'

    def __str__(self):
        return f'User {self.user_id} liked this post({self.liked_post})'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'User profile'
