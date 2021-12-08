from django.views.decorators.csrf import csrf_exempt
from authentication.views import check_and_remove_bearer, check_login
from django.http.response import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from authentication.models import AppUser
from course.models import Course
# from django.apps import apps
# AppUser = apps.get_model('authentication', 'AppUser')
# Create your views here.


@csrf_exempt
def catalogue(request):
    all_courses = Course.objects.all()
    response_object = []
    for course in all_courses.iterator():
        current_object = {}
        current_object['name'] = course.name
        current_object['author'] = course.author
        current_object['link'] = course.link
        response_object.append(current_object)

    print(response_object)
    return JsonResponse(response_object, safe=False)


@csrf_exempt
def addCourse(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        link = request.POST.get("link")
        # Filter out the channel name from the link url
        linkSplit = link.split("channel=")
        author = linkSplit[1]
        filtered_course = Course.objects.filter(name=name, link=link)
        if filtered_course.count() > 0:
            return HttpResponseForbidden("Course already exists")
        else:
            # Create new course if not already exists
            new_course = Course(name=name, author=author, link=link)
            new_course.save()
    return HttpResponse("add COurse")


def myCourses(request):
    print(request.headers['Authorization'])
    auth_header = request.headers['Authorization']
    auth_token = check_and_remove_bearer(auth_header)
    user_id = check_login(auth_token)
    if user_id is None:
        print("There was a issue with the token")
        return HttpResponseForbidden("The token was invalid")
    else:
        # write the code here
        course = AppUser.objects.get(pk=user_id).courses
        print(course)
        # check_login(request.headers)
        return HttpResponse("My course page!")


def getCourseById(request, course_id):
    print(course_id)
    return HttpResponse("CoursebyId")
