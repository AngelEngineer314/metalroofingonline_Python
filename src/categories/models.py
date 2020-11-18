from django.db import models

from tinymce import HTMLField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, null=True, unique=True)
    description = HTMLField('description')
    description_bottom = HTMLField('description')

    def __str__(self):
        return self.title