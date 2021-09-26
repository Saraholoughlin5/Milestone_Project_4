from django.urls import path
from . import views

# Adapted from Boutique Ado project

urlpatterns = [
    path('', views.index, name='home')
]
