from django.urls import path
from .views import (RegisterView,LoginView,UserListCreateView,UserDetailView,Meview,ProfileUpdateview)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),

    path("", UserListCreateView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),

    path("me/", Meview.as_view(),name="me"),
    path("profile/", ProfileUpdateview.as_view(),name="profile"),
]