from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.IntegerField(primary_key=True)

    # username = models.CharField(max_length=50, null=True, verbose_name='Имя пользователя')
    # имея username выводит ошибку users.CustomUser: (auth.E003) 'CustomUser.username' must be unique because it is named as the 'USERNAME_FIELD'.

    class Meta:
        verbose_name_plural = 'User'
