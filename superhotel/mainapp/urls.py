app_name='mainapp'

from django.urls import path
from django.urls import re_path
import mainapp.views as mainapp

urlpatterns = [
    path('contact/', mainapp.contact, name='contact'),
]