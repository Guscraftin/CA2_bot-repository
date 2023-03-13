# accounts/urls.py
from django.urls import path

from .views import SignUpView


# Redirection when at the end of url there are this path
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
