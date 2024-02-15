from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('runx3', views.runx3, name='runx3'),
    path('runx2', views.runx2, name='runx2'),
    path('runx', views.runx, name='runx'),
    path('run4', views.run4, name='run4'),
    path('run3', views.run3, name='run3'),
    path('run2', views.run2, name='run2'),
    path('run1', views.run1, name='run1'),
    path('hiragana', views.hiragana, name='hiragana'),
    path('hiragana2', views.hiragana2, name='hiragana2'),
]
