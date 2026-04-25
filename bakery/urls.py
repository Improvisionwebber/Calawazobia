from django.urls import path
from . import views
urlpatterns = [
    path('', views.bakery_home, name='bakery'),
]
