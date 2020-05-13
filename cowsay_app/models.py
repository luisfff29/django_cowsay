from django.db import models
import subprocess


# Create your models here.
class Main(models.Model):
    animals = subprocess.run(
        ['cowsay', '-l'], capture_output=True).stdout.decode().split()[4:]
    choose_animal = models.CharField(
        max_length=100, choices=((x, x) for x in animals))
    text = models.CharField(max_length=100)
    img = models.TextField()

    def __str__(self):
        return self.text
