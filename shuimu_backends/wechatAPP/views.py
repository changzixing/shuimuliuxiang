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
    # response = json.loads(requests.get(url).content)
    # if 'errcode' in response:
    #    return HttpResponse(response)

    # openid = response['openid']
    # session_key = response['session_key']
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
def get_activity(request):  # 小程序端获得活动列表，一个demo，需要后续修改与debug
    if request.method == 'GET':
        try:
            sortFlag = request.GET.get("sortFlag")  # 排序方式
            pageNum = request.GET.get("pageNum")  # 第几页
            pageNum = int(pageNum)
            actList = []
            if sortFlag == 'time':
                objActList = ActivityInfo.objects.filter().order_by('startDate')
                for i in objActList:
                    actList.append(i.activityName)
            elif sortFlag == 'hot':
                objActList = ActivityInfo.objects.filter().order_by('peopleCurrent')
                for i in objActList:
                    actList.append(i.activityName)
            else:
                pass

            resList = actList[pageNum*5:pageNum*5+5]
            res = {'content': resList}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such activityNum"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def edit_user(request):  # 编辑用户信息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        openid = request.POST.get("openID")
        try:
            user = UserInfo.objects.get(openID=openid)
            user.userSex = request.POST.get('sex')
            user.userZhiYuanBJ = request.POST.get('volunteerId')
            user.userPhone = request.POST.get('phoneNumber')
            user.userMail = request.POST.get('email')
            user.userInterest = request.POST.get('interest')
            user.userIntro = request.POST.get('introduction')
            user.save()
            res = {'result': 'edit succeeded'}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such user", "openid": openid}
            return HttpResponse(json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def send_user_info(request):  # 发送用户信息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        openid = request.POST.get("openID")
        try:
            user = UserInfo.objects.get(openID=openid)
            sex = user.userSex
            volunteerId = user.userZhiYuanBJ
            phoneNumber = user.userPhone
            email = user.userMail
            interest = user.userInterest
            introduction = user.userIntro
            res = {'sex': sex, 'volunteerId': volunteerId, 'phoneNumber': phoneNumber,
                   'email': email, 'interest': interest, 'introduction': introduction}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such user", "openid": openid}
            return HttpResponse(json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def send_activity_info(request):  # 发送活动信息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            activityNum = request.POST.get('activityNum')
            activity = ActivityInfo.objects.get(activityNum=activityNum)

            activityName = activity.activityName
            activityOwner = activity.activityOwner
            activityScore = activity.activityScore
            startDate = activity.startDate
            endDate = activity.endDate
            activityContact = activity.activityContact
            activityPoster = activity.activityPoster
            activityDescribe = activity.activityDescribe
            activityStatus = activity.activityStatus
            res = {'activityName': activityName, 'activityNum': activityNum, 'activityOwner': activityOwner,
                   'activityScore': activityScore, 'startDate': startDate, 'endDate': endDate,
                   'activityPoster': activityPoster, 'activityContact': activityContact,
                   'activityDescribe': activityDescribe, 'activityStatus': activityStatus}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such activity"}
            return HttpResponse(json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


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

        # img = request.FILES.get('photo')
        # if img:
        #   print('success')
        # models.ActivityInfo.objects.create(activityNum=activitynum, activityPoster=img)


def get_user_score(elem):
    return elem.userScore


def score_sort():
    users = UserInfo.objects.filter().order_by("userScore")
    sortList = []
    for i in users:
        sortList.append(i)
    # sortList.sort(key=get_user_score)
    return sortList


def user_count(activityNum):
    userList = TakePartIn.objects.filter(activityNum=activityNum)
    return len(userList)


@csrf_exempt
def send_message(request):  # 向所有参加用户发送信息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            activityNum = request.POST.get("activityNum")
            userID = request.POST.get("userID")
            users = TakePartIn.objects.filter(userID=userID)
            for i in users:
                UserInfo.objects.filter(userID=i.userID).update(hasNewMessage=1)
            mes = ActivityMessage()
            mes.activityNum = activityNum
            mes.messageContent = request.POST.get("messageContent")
            mes.save()
            res = {'content': 'successfully send'}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def get_message(request):  # 小程序端读取消息，一个demo，需要后续修改与debug
    if request.method == 'GET':
        try:
            activityNum = request.GET.get("activityNum")
            pageNum = request.GET.get("pageNum")
            pageNum = int(pageNum)
            objMsgList = ActivityMessage.objects.filter(activityNum=activityNum).order_by("createTime")
            msgList = []
            for i in objMsgList:
                msgList.append(i.messageContent)
            resList = msgList[pageNum*5:pageNum*5+5]
            res = {'content': resList}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such activityNum"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def join_activity(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            activityNum = request.POST.get("activityNum")
            userid = request.POST.get("userID")
            try:
                TakePartIn.objects.get(userID=userid)
                res = {'wrong': 'already joined in'}
                response = HttpResponse(json.dumps(res), status=200)
                return response
            except:
                try:
                    activity = ActivityInfo.objects.get(activityNum=activityNum)
                    member = TakePartIn()
                    member.groupID = activityNum
                    member.userID = userid
                    member.save()
                    temp = int(activity.peopleCurrent)
                    temp += 1
                    temp = str(temp)
                    ActivityInfo.objects.filter(activityNum=activityNum).update(peopleCurrent=temp)
                    res = {'1': 'succeed'}
                    response = HttpResponse(json.dumps(res), status=200)
                    return response
                except:
                    res = {'wrong': 'no such activity'}
                    response = HttpResponse(json.dumps(res), status=200)
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
            # render_to_response('homepage.html')
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
