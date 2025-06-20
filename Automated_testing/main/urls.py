# urls.py (main)
from django.urls import path
from .views import login

urlpatterns = [
    path('auth/sign-in', login),
]
