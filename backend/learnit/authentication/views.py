from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser
# Create your views here.


def Home(request):
    return HttpResponse("hi there ")


@csrf_exempt
def signup(request):

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
       # print(request.POST.get("email"))  # how to read variable from forms
        user = AppUser(email=email, password=password)
        user.save()
        print(user)
    return HttpResponse("good")
