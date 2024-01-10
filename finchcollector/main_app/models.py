from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    location = models.CharField(max_length=100, default='Unknown')
    description = models.TextField()

    def __str__(self):
        return self.name