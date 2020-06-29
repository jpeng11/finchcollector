from django.db import models

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=100)
    mass = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
