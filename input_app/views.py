from django.shortcuts import render
from . import forms

# Create your views here.


def home(request):
    return render(request, 'input_test.html',{"form":forms.InputForm()})