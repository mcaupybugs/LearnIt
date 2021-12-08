from authentication.views import check_and_remove_bearer, check_login
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from authentication.models import AppUser
# from django.apps import apps
# AppUser = apps.get_model('authentication', 'AppUser')
# Create your views here.


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
