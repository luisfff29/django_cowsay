from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def history(request):
    return render(request, 'history.html')
