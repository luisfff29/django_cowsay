from django.shortcuts import render
from cowsay_app.forms import TextInput
from cowsay_app.models import Main


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TextInput(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Main.objects.create(text=data['text'])
        return render(request, 'index.html', {'form': form})

    form = TextInput()

    return render(request, 'index.html', {'form': form})


def history(request):
    return render(request, 'history.html')
