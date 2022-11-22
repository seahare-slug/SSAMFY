from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup),
    path("profile/", views.profile),
    path("users/", views.get_users),
    path("liked/<int:movie_id>/", views.liked),
    path("liked/<str:username>/", views.liked_set),
]
