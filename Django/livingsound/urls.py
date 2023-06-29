from django.urls import path
from . import views


urlpatterns = [
    path("", views.garden, name="garden"),
    path("submission/", views.submission, name="submission"),  
    path("success", views.success, name="success")
]