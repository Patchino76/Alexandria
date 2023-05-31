from django.urls import path
from . import views

urlpatterns = [
    path('say_shit/', views.say_shit),
]