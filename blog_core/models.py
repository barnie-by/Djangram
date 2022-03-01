from django.db import models
from users.models import CustomUser


class Posts(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    content = models.TextField(null=True, blank=True, )
    published = models.DateTimeField(auto_now_add=True)

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
