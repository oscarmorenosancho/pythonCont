from django.urls import path
from . import views

urlpatterns = [
    path('', views.allMatchs, name="allmatchs"),
]
