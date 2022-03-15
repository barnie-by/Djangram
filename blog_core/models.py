from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from users.models import CustomUser
from uuid import uuid4


class Posts(models.Model):
    uniqueid = models.UUIDField(default=uuid4, unique=True, editable=False, help_text='post uuid')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self) -> str:
        return f'Post {self.id}, by {self.author}, {self.uniqueid}'

    def save(self, *args, **kwargs):
        value = self.content
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('post', kwargs={'post_slug': self.slug})
        # return reverse("post_detail", args=[self.uniqueid])
        return reverse('post', kwargs={'uuid': self.uniqueid})
        # kwargs = {
        #     # 'pk': self.id,
        #     'uniqueid': self.uniqueid
        # }
        # return reverse('post_detail', kwargs=kwargs)

    class Meta:
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    post = models.ForeignKey(Posts, on_delete=models.PROTECT)
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
