from django.urls import path
from . import views

urlpatterns = [
    path('book_listing/', views.book_listing),
]