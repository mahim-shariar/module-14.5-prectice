
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.modal_input,name='modal'),
]
