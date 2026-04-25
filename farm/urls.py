from django.urls import path
from . import views
urlpatterns = [
    path('', views.poultry, name='poultry'),
]
