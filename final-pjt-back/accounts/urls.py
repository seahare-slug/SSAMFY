from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup),
    path("profile/", views.profile),
    path("users/", views.get_users),
    # path("profile/liked/", views.liked),
]
