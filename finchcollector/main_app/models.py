from django.db import models
from django.urls import reverse

# Create your models here.
def upload_to_finch_image(instance, filename):
    return f'all-finches/{instance.id}/{filename}'

class Finch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to_finch_image, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
   