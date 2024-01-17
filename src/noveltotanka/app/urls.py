from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run3', views.run3, name='run3'),
    path('run2', views.run2, name='run2'),
    path('run1', views.run1, name='run1')
]
