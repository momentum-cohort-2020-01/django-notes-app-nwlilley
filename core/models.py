from django.db import models
from django.utils.text import slugify

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Note Title: {self.title} Body: {self.body} Date added: {self.created_at}"

class Tag(models.Model):
    name = models.CharField(max_length=40)
    slug = slugify(name)


