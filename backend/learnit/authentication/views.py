from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser
import jwt
import json
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


def get_token_from_header(token):
    PREFIX = 'Bearer '
    if not token.startswith(PREFIX):
        raise ValueError('Invalid Token')
    return token[len(PREFIX):]


def get_json_from_body(body):
    decoded_body = body.decode('utf-8')
    body_data = json.loads(decoded_body)
    return body_data


@csrf_exempt
def signup(request):

    if request.method == 'POST':
        try:
            body_data = get_json_from_body(request.body)
            # print(body_data['email'])
            email = body_data['email']
            password = body_data['password']
            print(email)
            print(password)
       # print(request.POST.get("email"))  # how to read variable from forms
       # raising the exception if the username already exists
            existingUser = AppUser.objects.filter(email=email)
            if existingUser.count() > 0:
                print("user already exists")
                return HttpResponseForbidden("Useralready exists")
            user = AppUser(email=email, password=password)
            user.save()
            print(user)
            return HttpResponse("good")
        except Exception as e:
            print(e)
            return HttpResponseBadRequest("Badd")


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            body_data = get_json_from_body(request.body)
            email = body_data['email']
            password = body_data['password']
            currentUser = AppUser.objects.filter(
                email=email, password=password)
            if currentUser.count() == 0:
                print('User not found')
                return HttpResponseForbidden("User not found")
            # print(currentUser)
            # print(currentUser[0].token)
            token = currentUser[0].token
        except Exception as e:
            print(e)
    return JsonResponse({'token': token})
