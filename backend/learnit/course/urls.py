from django.urls import path
from . import views
urlpatterns = [
    path("mycourse", views.myCourses, name="mycourse")
]
