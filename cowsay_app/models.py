from django.db import models
from cowsay_app.utils import list_of_animals


# Create your models here.
class Main(models.Model):
    choose_animal = models.CharField(
        max_length=100, choices=list_of_animals())
    text = models.CharField(max_length=100)
    img = models.TextField()

    def __str__(self):
        return self.text
