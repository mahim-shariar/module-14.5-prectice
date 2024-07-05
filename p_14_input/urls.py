
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('input_app.urls')),
    path('modal/',include('modal_input.urls')),
]
