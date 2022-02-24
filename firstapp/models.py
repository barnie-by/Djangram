from django.db import models
from users.models import CustomUser

class Posts (models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    photo = models.ForeignKey
    content = models.TextField(null=True, blank=True,)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Posts'

class Comments (models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey (CustomUser,on_delete=models.PROTECT)
    post = models.ForeignKey (Posts,on_delete=models.PROTECT)
    content = models.TextField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Comments'

class Likes (models.Model):
    id = models.IntegerField(primary_key=True)
    liked_post = models.ForeignKey(Posts,on_delete=models.PROTECT)
    user_id = models.ForeignKey (CustomUser,on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural='Likes'

class Media (models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.IntegerField

    class Meta:
        verbose_name_plural='Media'

