from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=240)
    # pub_date = models.DateTimeField('date added')


    def __str__(self):
        return f"Note Title: {self.title} Body: {self.body}"

