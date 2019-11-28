from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from wechatAPP import models
from .models import ActivityInfo, ActivityMessage
from .models import UserInfo
from .models import TakePartIn
from .models import GroupMember
import time
import requests
import json
import random
import string
import hashlib
from datetime import datetime, date, timedelta
from django.http import HttpResponse

appid = 'wx5131007b3004e250'
secret = '6106f01b6fa163b986da283e98cf7ccb'

@csrf_exempt
def wechat_login(request):
    js_code = request.POST.get('code')
    url = 'https://api.weixin.qq.com/sns/jscode2session' + '?appid=' + appid + '&secret=' + secret + '&js_code=' + js_code + '&grant_type=authorization_code'
    #response = json.loads(requests.get(url).content)
    #if 'errcode' in response:
    #    return HttpResponse(response)

    #openid = response['openid']
    #session_key = response['session_key']
    openid = 'oo85p5LEN2BJ8rf1WJE0m03iM0lY'
    session_key = 'e867Drf5jj56PkEyO9wJhg=='

    users = models.UserInfo.objects.filter(openID=openid)
    if len(users) == 0:
        res = {"error": "no such user", "openid": openid}
        return HttpResponse(json.dumps(res), status=200)
    res = {"openid": openid, "session_key": session_key}
    return HttpResponse(json.dumps(res), status=200)


def wechat_identity(request):
    if request.method == 'POST':
        try:
            openid = request.POST.get("openid")
            token = request.POST.get("token")
            url = 'https://alumni-test.iterator-traits.com/fake-id-tsinghua-proxy/api/user/session/token'
            data = {'token': token}
            response = json.loads(requests.post(url, data=json.dumps(data)))
            if response['user']['error']['code'] != 0:
                res = {'error': 'no such student'}
                return HttpResponse(content=json.dumps(res), status=201)
            user = response['user']
            username = user['name']
            card = user['card']
            department = user['department']
            models.UserInfo.objects.create(userName=username, userID=card, department=department, openID=openid)
            return HttpResponse(json.dumps(user))
        except:
            res = {'error': 'wrong'}
            return HttpResponse(content=json.dumps(res), status=400)


@csrf_exempt
def test(request):
    if request.method == "POST":
        activityName = request.POST.get('activityName')
        activitynum = request.POST.get('activityNum')
        activityOwner = request.POST.get('activityOwner')
        activity = ActivityInfo()
        activity.activityNum = activitynum
        activity.activityPoster = request.FILES.get('photo')
        activity.activityContact = request.FILES.get('scancode')
        activity.save()

        res = {'1': '1'}
        return HttpResponse(content=json.dumps(res), status=200)

        #img = request.FILES.get('photo')
        #if img:
        #   print('success')
        #models.ActivityInfo.objects.create(activityNum=activitynum, activityPoster=img)


def get_user_score(elem):
    return elem.userScore


def score_sort():
    users = UserInfo.objects.filter()
    sortlist=[]
    for i in users:
        sortlist.append(i)
    sortlist.sort(key=getuserscore)
    return sortlist


def user_count(activitynum):
    userlist = TakePartIn.objects.filter(activityNum=activitynum)
    return len(userlist)


@csrf_exempt
def send_message(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            activitynum = request.POST.get("activityNum")
            userID = request.POST.get("userID")
            users = TakePartIn.objects.filter(userID=userID)
            for i in users:
                UserInfo.objects.filter(userID=i.userID).update(hasNewMessage = 1)
            mes = ActivityMessage()
            mes.activityNum = activitynum
            mes.messageContent = request.POST.get("messageContent")
            res = {'1': '1'}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def join_group(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            groupid = request.POST.get("groupID")
            userid = request.POST.get("userID")
            try:
                users = GroupMember.objects.get(userID=userid)
                res = {'wrong': 'already joined in'}
                response = HttpResponse(json.dumps(res), status=200)
                return response
            except:
                member = GroupMember()
                member.groupID = groupid
                member.userID = userid
                member.save()
                res = {'1': 'succeed'}
                response = HttpResponse(json.dumps(res), status=200)
                return response
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def create_activity(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            activity = ActivityInfo()
            activity.activityName = request.POST.get('activityName')
            activity.activityNum = request.POST.get('activityNum')
            activity.activityOwner = request.POST.get('activityOwner')
            activity.activityScore = request.POST.get('activityScore')
            activity.activityDescribe = request.POST.get('activityDescribe')
            activity.activityPoster = request.FILES.get('photo')
            activity.activityContact = request.FILES.get('scanCode')
            activity.startDate = request.POST.get('startDate')
            activity.endDate = request.POST.get('endDate')
            activity.save()

            res = {"activity_created": "1"}
            return HttpResponse(content=json.dumps(res), status=200)
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


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
            users = models.UserInfo.objects.filter(username=username)
            if len(users) > 0:
                res = {"error": "user exists"}
                return HttpResponse(json.dumps(res))
            models.UserInfo.objects.create(username=username, password=password, session_id='0')
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
            users = models.UserInfo.objects.filter(username=username)
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
            models.UserInfo.objects.filter(username=username).update(session_id=session)
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
            users = models.UserInfo.objects.filter(session_id=cookies)
            if len(users) == 0:
                res = {"error": "no valid session2"}
                return HttpResponse(json.dumps(res))
            models.UserInfo.objects.filter(username=users[0].username).update(session_id="0")
            res = {"user": users[0].username}
            return HttpResponse(json.dumps(res))
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        if request.method != "POST":
            res = {"error": "require POST"}
