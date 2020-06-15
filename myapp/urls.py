from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second_base', views.second_base, name='second_base'),
]
