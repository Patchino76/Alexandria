from django.urls import path
from . import views

urlpatterns = [
    path('profile_listing/', views.profile_listing),
    path('profile/<int:profile_id>/',  views.profile)
]