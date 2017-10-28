from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Author(models.Model):
    user_name = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name


class Publisher(models.Model):
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class Page(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


