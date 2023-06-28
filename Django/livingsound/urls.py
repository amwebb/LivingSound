from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.garden, name="garden"),
    path("submission/", views.submission, name="submission"),
    path("accounts/", include("django.contrib.auth.urls"))  
]