from django.http.response import Http404, HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser
import jwt
from django.conf import settings

# Create your views here.


def check_login(token):
    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms='HS256')
        print(decoded_token)
        return decoded_token['id']
    except:
        print("Invalid signature")
        return None

# function to check and remove the bearer from the front


def check_and_remove_bearer(token):
    PREFIX = 'Bearer '
    if not token.startswith(PREFIX):
        raise ValueError('Invalid Token')
    return token[len(PREFIX):]


def Home(request):
    return HttpResponse("hi there ")


@csrf_exempt
def signup(request):

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
       # print(request.POST.get("email"))  # how to read variable from forms
       # raising the exception if the username already exists
        existingUser = AppUser.objects.filter(email=email)
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
        # print(currentUser)
        # print(currentUser[0].token)
        token = currentUser[0].token
    return JsonResponse({'token': token})
