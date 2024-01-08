from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run3', views.run3, name='run3'),
]
