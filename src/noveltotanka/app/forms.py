from django import forms

class WordForm():
    word = forms.CharField(max_length=100)
