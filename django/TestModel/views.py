from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django_redis import get_redis_connection
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from TestModel import models
import time
import requests
import json
import random
import string
import hashlib
from datetime import datetime
from django.http import HttpResponse

appid = ''
secret = ''

@csrf_exempt
def wechat_login(request):
    js_code = request.data['code']
    url = 'https://api.weixin.qq.com/sns/jscode2session' + '?appid=' + appid + '&secret=' + secret + '&js_code=' + js_code + '&grant_type=authorization_code'
    response = json.loads(requests.get(url).content)

    if 'errcode' in response:
        return HttpResponse(data={'code': response['errcode'], 'msg': response['errmsg']})

    openid = response['openid']
    session_key = response['session_key']

    #user, created = models.User.objects.get_or_create(openid=openid)
    users = models.User.objects.filter(openID=openid)
    if len(users) > 0:
        res = {"error": "has logged in"}
        return HttpResponse(json.dumps(res))
    user_str = serializers.serialize('json', users[0]).data
    sha = hashlib.sha1()
    sha.update(openid.encode())
    sha.update(session_key.encode())
    digest = sha.hexdigest()
    # 将自定义登录态保存到缓存中, 两个小时过期
    conn = get_redis_connection('default')
    conn.set(digest, user_str, ex=2 * 60 * 60)
    return HttpResponse(data={'code': 200, 'msg': 'ok', 'data': {'skey': digest}})


@csrf_exempt
def logon(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username)
            print(password)
            if len(username) == 0 or len(password) == 0:
                res = {"error": "invalid parameters"}
                return HttpResponse(json.dumps(res))
            users = models.User.objects.filter(username=username)
            if len(users) > 0:
                res = {"error": "user exists"}
                return HttpResponse(json.dumps(res))
            models.User.objects.create(username=username, password=password, session_id='0')
            res = {"user": username}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            users = models.User.objects.filter(username=username)
            if len(username) == 0 or len(users) == 0:
                res = {"error": "no such a user"}
                return HttpResponse(json.dumps(res))
            if users[0].password != password:
                res = {"error": "password is wrong"}
                return HttpResponse(json.dumps(res))
            if users[0].session_id != "0":
                res = {"error": "has logged in"}
                return HttpResponse(json.dumps(res))
            session = ''.join(random.sample(string.ascii_letters + string.digits, 16))
            models.User.objects.filter(username=username).update(session_id=session)
            res = {"user": username}
            response = HttpResponseRedirect('homepage')
            response["Set-Cookie"] = "session_id=" + session
            response.write(json.dumps(res))
            return response
            #, render_to_response('homepage.html')
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        try:
            cookies = request.COOKIES.get("session_id")
            print("cookies")
            print(cookies)
            if len(cookies) < 2:
                res = {"error": "no valid session1"}
                return HttpResponse(json.dumps(res))
            users = models.User.objects.filter(session_id=cookies)
            if len(users) == 0:
                res = {"error": "no valid session2"}
                return HttpResponse(json.dumps(res))
            models.User.objects.filter(username=users[0].username).update(session_id="0")
            res = {"user": users[0].username}
            return HttpResponse(json.dumps(res))
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        if request.method != "POST":
            res = {"error": "require POST"}
