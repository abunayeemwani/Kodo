from curses import meta
from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    description = models.TextField()
    dateLastEdited = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Data"