from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)




