from django.shortcuts import render
from cowsay_app.forms import TextInput
from cowsay_app.models import Main
import subprocess


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TextInput(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Main.objects.create(text=data['text'])
            result = subprocess.run(
                ['cowsay'] + data['text'].split(), capture_output=True).stdout.decode()
        return render(request, 'index.html', {'form': form, 'result': result})

    form = TextInput()

    return render(request, 'index.html', {'form': form})


def history(request):
    return render(request, 'history.html')
