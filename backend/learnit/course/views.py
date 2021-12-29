from django.http import response
from django.views.decorators.csrf import csrf_exempt
from authentication.views import get_token_from_header, check_login
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
        current_object['course_id'] = course.id
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
    # print(request.headers['Authorization'])
    print(request.headers)
    auth_header = request.headers['Authorization']
    auth_token = get_token_from_header(auth_header)
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
    fetchedCourse = Course.objects.get(pk=course_id)
    response_object = {}
    response_object['course_id'] = fetchedCourse.id
    response_object['name'] = fetchedCourse.name
    response_object['author'] = fetchedCourse.author
    response_object['link'] = fetchedCourse.link
    # print(response_object)
    return JsonResponse(response_object)


def buyCourse(request, course_id):
    try:
        auth_header = request.headers['Authorization']
        auth_token = get_token_from_header(auth_header)
        user_id = check_login(auth_token)
        if user_id is None:
            print("There was a issue with the token")
            return HttpResponseForbidden("You need to login first")

        fetched_course = Course.objects.get(pk=course_id)
        print(fetched_course)
        if fetched_course == None:
            return HttpResponseForbidden("Invalid course Id")
        fetched_user = AppUser.objects.get(pk=user_id)
        if fetched_user == None:
            return HttpResponseForbidden("no user found")
        print(fetched_user.courses)
        does_user_already_contain_course = fetched_user.courses.filter(
            pk=fetched_course.id)
        if does_user_already_contain_course:
            return HttpResponseForbidden("Course already bought")
        else:
            fetched_user.courses.add(fetched_course)
            fetched_user.save()
        return HttpResponse("Course Bought")
    except Exception as e:
        print(e)
        return HttpResponseForbidden("An exception occured")
