from django.db import models


# Create your models here.
class CowText(models.Model):
    text = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.text
