from django.shortcuts import render
from cowsay_app.forms import TextInput
from cowsay_app.models import Main
from cowsay_app.utils import output


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TextInput(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = TextInput()
            result = output(data)
            Main.objects.create(text=data['text'], img=result)
        return render(request, 'index.html', {'form': form, 'result': result})

    form = TextInput()

    return render(request, 'index.html', {'form': form})


def history(request):
    data = Main.objects.order_by('-id')[:10]
    return render(request, 'history.html', {'data': data})
