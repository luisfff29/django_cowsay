from django.db import models


# Create your models here.
class Main(models.Model):
    text = models.CharField(max_length=100)
    img = models.TextField()

    def __str__(self):
        return self.text
