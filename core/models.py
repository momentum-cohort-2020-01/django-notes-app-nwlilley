from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Note Title: {self.title} Body: {self.body} Date added: {self.created_at}"

