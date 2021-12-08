from os import name
from django.urls import path
from . import views
urlpatterns = [
    path("mycourse", views.myCourses, name="mycourse"),
    path('catalogue', views.catalogue, name="catalogue"),
    path('addCourse', views.addCourse, name="addCourse"),
    path('course/<int:course_id>', views.getCourseById, name="courseId"),
    path('buycourse/<int:course_id>', views.buyCourse, name='buycourse')
]
