from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time = models.DateTimeField()

    def __str__(self):
        return self.text