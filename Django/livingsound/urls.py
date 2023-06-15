from django.urls import path
from livingsound import views

urlpatterns = [
    path("", views.garden, name="garden"),
]