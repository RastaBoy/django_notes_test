from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=255) # hash из email + password
    dt_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
        ordering = ['dt_create']


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Заметки"
        verbose_name_plural = "Заметки"
        ordering = ['dt_create']




