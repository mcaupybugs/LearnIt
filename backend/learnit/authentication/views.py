from django.http.response import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
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
       # raising the exception if the username already exists
        existingUser = AppUser.objects.filter(email=email, password=password)
        if existingUser.count() > 0:
            return HttpResponseForbidden("Useralready exists")
        user = AppUser(email=email, password=password)
        user.save()
        print(user)
    return HttpResponse("good")


@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        currentUser = AppUser.objects.filter(email=email, password=password)
        if currentUser.count() == 0:
            return HttpResponseForbidden("User not found")
        print(currentUser)
        # print(currentUser[0].token)
        token = currentUser[0].token
    return JsonResponse({'token': token})
