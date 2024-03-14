from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .tokens import *
from .models import Token
from transcendence.settings import SECRET_KEY

import json

# Create your views here.
def info(request):
    return JsonResponse({'msg':'INFO'})

def about(request):
    return JsonResponse({'msg':'ABOUT'})

def match(request, id):
    return JsonResponse({'msg':'MATCH', 'id':id})

def getData(request):
    return JsonResponse({'msg':'DATA'})

def findTokens(request, **kwargs):
    for key, value in kwargs.items():
        if (key == 'all' and value==True):
            objs = Token.objects.filter(owner=request.user)
            break
        if (key == 'used'):
            objs = Token.objects.filter(owner=request.user, used=value)
            break
        objs = Token.objects.filter(owner=request.user, used=False)
    res = []
    if (objs):
        for obj in objs:
            res.append({'id': obj.id})
    return res

def appendTokenInDb(owner:str, token:str):

    if owner and token:
        usr = User.objects.filter(username=owner).first()
        print (usr)
        if (usr):
            Token.objects.create(id=token, owner=usr)


@csrf_exempt
def getTokens(request):
    return JsonResponse(findTokens(request=request, all=1), safe=False)

@csrf_exempt
def signupToken(request):
    ret = {"access":"", "refresh":""}
    if (request.method == 'POST'):
        body_data = json.loads(request.body)
        login_username = body_data['username']
        login_email = body_data['email']
        login_password1 = body_data['password1']
        login_password2 = body_data['password2']
        if (login_password1 != login_password2):
            ret = { 'errormsg': 'Repeated password must be equal to password' }
            return JsonResponse( ret )
        usr = User.objects.filter(username=login_username).first()
        if (usr):
            ret = { 'errormsg': 'Can not create this user, already exists' }
            return JsonResponse( ret )
        print ({'username': login_username, 'password': login_password1,  'email':login_email})
        usr = User.objects.create_user(username=login_username, password=login_password1, email=login_email)
        print ("User", usr)
        if (not usr):
            ret = { 'errormsg': 'Can not create this user' }
            return JsonResponse( ret )
        usr.save()
        ret['username'] = usr.get_username()
        ret['access'] = getToken({'username': usr.get_username() }, SECRET_KEY)
        appendTokenInDb(owner=login_username, token=ret['access'])
        print (ret)
        ret['refresh'] = getToken({'username': usr.get_username() }, SECRET_KEY)
        appendTokenInDb(owner=login_username, token=ret['refresh'])
        print(ret)
        return JsonResponse( ret )
    ret = { 'errormsg': 'This is not a POST request' }
    return JsonResponse( ret )

@csrf_exempt
def loginToken(request):
    ret = {"access":"", "refresh":""}
    if (request.method == 'POST'):
        body_data = json.loads(request.body)
        login_username = body_data['username']
        login_password = body_data['password']
        usr = User.objects.filter(username=login_username).first()
        if (not usr or not usr.check_password(login_password)):
            ret = { 'errormsg': 'Either username or password are incorrect' }
            return JsonResponse( ret )
        ret['access'] = getToken({'username': login_username }, SECRET_KEY, True)
        appendTokenInDb(owner=login_username, token=ret['access'])
        ret['refresh'] = getToken({'username': login_username }, SECRET_KEY, False)
        appendTokenInDb(owner=login_username, token=ret['refresh'])
        ret['username'] = login_username
        print({ **request.POST, **ret })
        return JsonResponse( ret )
    ret = { 'errormsg': 'This is not a POST request' }
    return JsonResponse( ret )

@csrf_exempt
def refreshToken(request):
    ret = {"access":"", "refresh":""}
    if (request.method == 'POST'):
        body_data = json.loads(request.body)
        refreshToken = body_data['refresh']
        decoded_data = verifyToken(refreshToken, SECRET_KEY)
        username = decoded_data['username']
        tokentype = decoded_data['tokentype']
        if tokentype == 'refresh' and username:
            ret['access'] = getToken({'username': username }, SECRET_KEY, True)
            appendTokenInDb(owner=username, token=ret['access'])
            ret['refresh'] = getToken({'username': username }, SECRET_KEY, False)
            appendTokenInDb(owner=username, token=ret['refresh'])
            ret['username'] = username
            return JsonResponse( ret )
        ret = { 'errormsg': 'There is not a valid Refresh Token' }
        return JsonResponse( ret )
    ret = { 'errormsg': 'This is not a POST request' }
    return JsonResponse(ret)

@csrf_exempt
def logoutToken(request):
    ret = {"access":"", "refresh":""}
    if (request.method == 'POST'):
        body_data = json.loads(request.body)
        accessToken = body_data['access']
        decoded_data = verifyToken(accessToken, SECRET_KEY)
        username = decoded_data['username']
        tokentype = decoded_data['tokentype']
        if tokentype == 'access' and username:
            ret['username'] = username
            ret['msg'] = 'logged out'
            return JsonResponse( ret )
        ret = { 'errormsg': 'There is not a valid Refresh Token' }
        return JsonResponse( ret )
    ret = { 'errormsg': 'This is not a POST request' }
    return JsonResponse(ret)


