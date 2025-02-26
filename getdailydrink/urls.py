from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.challenge, name='challenge'),
    path('rewards/', views.rewards, name='rewards'),
    path('log_water/', views.log_water, name='log_water'),
]