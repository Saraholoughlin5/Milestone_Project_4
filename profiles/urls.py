from django.urls import path
from . import views

# Adapted from Boutique Ado project

urlpatterns = [
    path('', views.profile, name='profile'),    
    path('order_history/<order_number>', views.order_history, name='order_history'),
]
