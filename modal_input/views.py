from django.shortcuts import render
from . import forms

# Create your views here.


def modal_input(request):
    return render(request, 'modal_input.html',{"form":forms.ModalForm()})