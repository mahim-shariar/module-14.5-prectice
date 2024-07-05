from django import forms
from .models import modalInput

class ModalForm(forms.ModelForm):
   
    class Meta:
        model = modalInput
        fields = "__all__"