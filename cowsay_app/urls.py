from django.urls import path
from cowsay_app import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('history/', views.history, name='history')
]
