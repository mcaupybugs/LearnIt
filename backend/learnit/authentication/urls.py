from django.urls import path
from . import views
urlpatterns = [
    path("", views.Home, name="startingPage"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
]
