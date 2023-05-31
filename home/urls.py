from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.sample),
    path('about/', views.about),
    # path('', views.home)
]