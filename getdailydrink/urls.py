from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_water, name='log_water'),
]