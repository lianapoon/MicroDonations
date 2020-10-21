from django.urls import path
from django.urls import include, path
from django.views.generic import TemplateView  # <--

from . import views

app_name = 'donations'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]
