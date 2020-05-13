from django import forms
from cowsay_app.utils import list_of_animals


class TextInput(forms.Form):
    choose_animal = forms.ChoiceField(
        choices=list_of_animals(), initial='default')
    text = forms.CharField(widget=forms.TextInput())
