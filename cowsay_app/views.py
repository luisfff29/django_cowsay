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
            form = TextInput()
            if data['choose_animal'] == 'default':
                result = subprocess.run(
                    ['cowsay'] + data['text'].split(), capture_output=True).stdout.decode()
            else:
                result = subprocess.run(
                    ['cowsay'] + ['-f'] + [data['choose_animal']] + data['text'].split(), capture_output=True).stdout.decode()
            Main.objects.create(text=data['text'], img=result)
        return render(request, 'index.html', {'form': form, 'result': result})

    form = TextInput()

    return render(request, 'index.html', {'form': form})


def history(request):
    data = Main.objects.order_by('-id')[:10]
    return render(request, 'history.html', {'data': data})
