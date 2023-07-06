from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path("", views.garden, name="garden"),
    path("submission/", views.submission, name="submission"),  
    path("success", views.success, name="success"),
    path("accounts/", include("django.contrib.auth.urls")),  
    re_path(r'^posts/(?P<username>\w+)/$', views.profile, name="profile"),

]