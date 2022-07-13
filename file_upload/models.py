from django.db import models
from django.http import HttpResponseBadRequest

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/csvs/')

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)