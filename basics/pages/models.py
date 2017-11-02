from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Page(models.Model):

    title = models.CharField(max_length=90)
    content = RichTextField()

    def __str__(self):
        return self.title


