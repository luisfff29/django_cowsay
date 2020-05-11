from django.db import models


# Create your models here.
class Main(models.Model):
    text = models.CharField()

    def __str__(self):
        return self.text
