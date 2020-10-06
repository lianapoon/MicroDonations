from django.urls import path
from django.urls import include, path
from django.views.generic import TemplateView  # <--

from . import views

app_name = 'donations'
urlpatterns = [
    path('', views.index, name='index'),
]
