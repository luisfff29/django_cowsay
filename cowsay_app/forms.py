from django import forms
import subprocess


class TextInput(forms.Form):
    animals = subprocess.run(
        ['cowsay', '-l'], capture_output=True).stdout.decode().split()[4:]
    choose_animal = forms.ChoiceField(
        choices=((x, x) for x in animals), initial='default')
    text = forms.CharField(widget=forms.TextInput())
