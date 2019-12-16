import jieba
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from wechatAPP import models
from .models import ActivityInfo, ActivityMessage
from .models import UserInfo
from .models import TakePartIn
from .models import GroupInfo
from .models import GroupMember
from .models import Administrator
import time
import requests
import json
import random
import string
import hashlib
import xlwt
from datetime import datetime, date, timedelta

appid = 'wx5131007b3004e250'
secret = '6106f01b6fa163b986da283e98cf7ccb'


@csrf_exempt
def homepage(request):
    return HttpResponse(content='hompage')


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


@csrf_exempt
def wechat_identity(request):
    if request.method == 'POST':
        try:
            '''user = UserInfo()
            user.openID = 'oo85p5LEN2BJ8rf1WJE0m03iM0l3'
            user.userName = 'huqian3'
            user.userScore = 300
            user.department = 'THSS'
            user.userID = '333333333'
            user.save()'''
            openid = request.POST.get("openid")
            token = request.POST.get("token")
            users = models.UserInfo.objects.filter(openID=openid)
            if len(users) != 0:
                res = {'error': 'already logged on'}
                return HttpResponse(json.dumps(res), status=200)
            url = 'https://alumni-test.iterator-traits.com/fake-id-tsinghua-proxy/api/user/session/token'
            data = {'token': token}
            res = requests.post(url, data=data)
            info = json.loads(res.content)
            try:
                user = UserInfo()
                user.openID = openid
                user.userName = info['user']['name']
                user.userID = info['user']['card']
                user.department = info['user']['department']
                user.save()
                return HttpResponse(content=res)
            except:
                return HttpResponse(content=json.dumps({'error': 'not a student'}), status=200)

        except:
            res = {'error': 'wrong'}
            return HttpResponse(content=json.dumps(res), status=400)


@csrf_exempt
def search_activity(request):  # 目前完成了按名字搜索
    if request.method == 'POST':
        try:
            searchKeyword = request.POST.get('searchKeyword')
            seg_list = jieba.cut_for_search(searchKeyword)
            seg_list.sort(key=lambda x: len(x), reverse=True)
            searchFlag = request.POST.get("searchFlag")  # 搜索方式
            if searchFlag is None:  # 默认按名称搜索
                searchFlag = 'name'
            pageNum = request.POST.get("pageNum")  # 第几页
            if pageNum is None:  # 默认第一页
                pageNum = '1'
            pageNum = int(pageNum) - 1
            actList = []
            if searchFlag == 'name':
                for j in seg_list:
                    objActList = ActivityInfo.objects.filter(activityName__contains=j)
                    if len(objActList) != 0:
                        for i in objActList:
                            temp = {'name': i.activityName, 'startDate': i.startDate.strftime('%Y-%m-%d'),
                                    'owner': i.activityOwner, 'peopleNeed': i.peopleNeed,
                                    'peopleCurrent': i.peopleCurrent,
                                    'type': i.activityType, 'address': i.activityAddress}
                            actList.append(temp)
            elif searchFlag == 'owner':
                for j in seg_list:
                    objActList = ActivityInfo.objects.filter(activityOwner__contains=j)
                    if len(objActList) != 0:
                        for i in objActList:
                            temp = {'name': i.activityName, 'startDate': i.startDate.strftime('%Y-%m-%d'),
                                    'owner': i.activityOwner, 'peopleNeed': i.peopleNeed,
                                    'peopleCurrent': i.peopleCurrent,
                                    'type': i.activityType, 'address': i.activityAddress}
                            actList.append(temp)
            else:
                pass

            resList = actList[pageNum * 5:pageNum * 5 + 5]
            res = {'content': resList}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such activityNum"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def get_activity(request):  # 小程序端获得活动列表，一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            objActList = ActivityInfo.objects.filter()
            actList = []

            sortFlag = request.POST.get("sortFlag")  # 排序方式
            if sortFlag is None or len(sortFlag) == 0:  # 默认按时间排序
                sortFlag = 'time'

            pageNum = request.POST.get("pageNum")  # 第几页
            if pageNum is None or len(pageNum) == 0:  # 默认第一页
                pageNum = '1'
            pageNum = int(pageNum) - 1

            searchKeyword = request.POST.get('searchKeyword')  # 搜索关键字
            seg_list = []
            if searchKeyword is not None and len(searchKeyword) != 0:
                seg_list = jieba.cut_for_search(searchKeyword)
                if len(seg_list) != 0:
                    seg_list.sort(key=lambda x: len(x), reverse=True)

            searchFlag = request.POST.get("searchFlag")  # 搜索类别，如名字、组织者等
            if searchFlag is None:  # 默认按名称搜索
                searchFlag = 'name'

            activityType = request.POST.get('activityType')  # 筛选类型，如文教等
            if activityType is not None:
                for i in activityType:
                    objActList = objActList.filter(activityType=i)

            activityStatus = request.POST.get('activityStatus')  # 活动状态，如报名中等
            if activityStatus is not None:
                objActList.filter(activityStatus=activityStatus)

            if len(seg_list) != 0:  # 如果搜索栏不为空，则开始搜索
                if searchFlag == 'name':
                    objActList = objActList.filter(activityName__contains=seg_list[0])
                    for j in seg_list[1:]:
                        tempActList = ActivityInfo.objects.filter(activityName__contains=j)
                        objActList = objActList | tempActList
                    # objActList.order_by('activityNum').distinct('activityNum')  # 去重
                elif searchFlag == 'owner':
                    objActList = objActList.filter(activityName__contains=seg_list[0])
                    for j in seg_list[1:]:
                        tempActList = ActivityInfo.objects.filter(activityName__contains=j)
                        objActList = objActList | tempActList
                    # objActList.order_by('activityNum').distinct('activityNum')  # 去重
                else:
                    res = {"error": "wrong searchFlag"}
                    return HttpResponse(content=json.dumps(res), status=200)

            if len(objActList) == 0:
                res = {"warning": "empty search!"}
                return HttpResponse(content=json.dumps(res), status=200)

            # 搜索完成后，或搜索栏为空
            if sortFlag == 'time':  # 按时间排序
                objActList = objActList.order_by('-startDate')
                print(len(objActList))
                for i in objActList:
                    temp = {'name': i.activityName, 'startDate': i.startDate.strftime('%Y-%m-%d'),
                            'owner': i.activityOwner, 'peopleNeed': i.peopleNeed, 'peopleCurrent': i.peopleCurrent,
                            'type': i.activityType, 'address': i.activityAddress}
                    actList.append(temp)
            elif sortFlag == 'hot':  # 按热度排序
                objActList = objActList.order_by('peopleCurrent')
                for i in objActList:
                    temp = {'name': i.activityName, 'startDate': i.startDate.strftime('%Y-%m-%d'),
                            'owner': i.activityOwner, 'peopleNeed': i.peopleNeed, 'peopleCurrent': i.peopleCurrent,
                            'type': i.activityType, 'address': i.activityAddress}
                    actList.append(temp)
            elif sortFlag == 'notFull':  # 未招满
                objActList = objActList.filter(peopleNeed__gt=F('peopleCurrent')).order_by('peopleCurrent')
                for i in objActList:
                    temp = {'name': i.activityName, 'startDate': i.startDate.strftime('%Y-%m-%d'),
                            'owner': i.activityOwner, 'peopleNeed': i.peopleNeed, 'peopleCurrent': i.peopleCurrent,
                            'type': i.activityType, 'address': i.activityAddress}
                    actList.append(temp)
            else:
                res = {"error": "wrong sortFlag"}
                return HttpResponse(content=json.dumps(res), status=200)

            resList = actList[pageNum * 4:pageNum * 4 + 4]  # 一页四个
            res = {'content': resList}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such activityNum"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def edit_user(request):  # 编辑用户信息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        openid = request.POST.get("openID")
        if openid is None:
            res = {'wrong': 'no openID'}
            response = HttpResponse(json.dumps(res))
            return response
        try:
            user = UserInfo.objects.get(openID=openid)
            userSex = request.POST.get('sex')
            if userSex is not None:
                user.userSex = userSex
            userZhiYuanBJ = request.POST.get('volunteerId')
            if userZhiYuanBJ is not None:
                user.userZhiYuanBJ = userZhiYuanBJ
            userPhone = request.POST.get('phoneNumber')
            if userPhone is not None:
                user.userPhone = userPhone
            userMail = request.POST.get('email')
            if userMail is not None:
                user.userMail = userMail
            userInterest = request.POST.get('interest')
            if userInterest is not None:
                user.userInterest = userInterest
            userIntro = request.POST.get('introduction')
            if userIntro is not None:
                user.userIntro = userIntro
            user.save()
            res = {'result': 'edit succeeded'}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such user", "openID": openid}
            return HttpResponse(json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def send_user_info(request):  # 发送用户信息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        openid = request.POST.get("openID")
        if openid is None:
            res = {"error": "no openID"}
            return HttpResponse(json.dumps(res), status=200)
        try:
            user = UserInfo.objects.get(openID=openid)
            sex = user.userSex
            studentId = user.userID
            department = user.department
            volunteerId = user.userZhiYuanBJ
            phoneNumber = user.userPhone
            email = user.userMail
            interest = user.userInterest
            introduction = user.userIntro
            res = {'sex': sex, 'volunteerId': volunteerId, 'studentId': studentId,
                   'department': department, 'phoneNumber': phoneNumber,
                   'email': email, 'interest': interest, 'introduction': introduction}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such user", "openid": openid}
            return HttpResponse(json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


#@csrf_exempt
#def testhtml(request):
#    #return render(request, 'test.html')
#    return render(request, 'login.html')


@csrf_exempt
def get_approve_list(request):
    activities = ActivityInfo.objects.filter(activityStatus='-1')
    res = []
    for activity in activities:
        activityinfo = {}
        activityinfo['headline'] = activity.activityName
        activityinfo['date'] = '开始日期: '+str(activity.startDate) + ' 结束日期: '+str(activity.endDate)
        activityinfo['describe'] = activity.activityDescribe
        activityinfo['number'] = activity.peopleNeed
        activityinfo['place'] = activity.activityAddress
        activityinfo['picture'] = 'media/' + str(activity.activityPoster)
        res.append(activityinfo)
    return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def send_activity_info(request):  # 发送活动信息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            activityNum = request.POST.get('activityNum')
            if len(activityNum) == 0:
                res = {"error": "no activityNum"}
                return HttpResponse(json.dumps(res), status=200)
            activity = ActivityInfo.objects.get(activityNum=activityNum)
            activityName = activity.activityName
            activityOwner = activity.activityOwner
            activityScore = activity.activityScore
            startDate = activity.startDate.strftime("%Y-%m-%d")
            endDate = activity.endDate.strftime("%Y-%m-%d")
            # activityContact = activity.activityContact
            activityPoster = str(activity.activityPoster)
            # activityDescribe = activity.activityDescribe
            # activityStatus = activity.activityStatus
            res = {'activityName': activityName, 'activityNum': activityNum, 'activityOwner': activityOwner,
                   'activityScore': activityScore, 'startDate': startDate, 'endDate': endDate,
                   'activityPoster': activityPoster, }  # 'activityContact': activityContact,
            # 'activityDescribe': activityDescribe, 'activityStatus': activityStatus}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such activity"}
            return HttpResponse(json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


'''@csrf_exempt
def test(request):
    if request.method == "POST":
        username = 'administrator'
        password = '123456'
        password = hashlib.md5(password.encode()).hexdigest()
        user = Administrator()
        user.username = username
        user.password = password
        user.sessionID = '0'
        user.save()
        res = {'1': '1'}
        return HttpResponse(content=json.dumps(res), status=200)'''



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
            TakePartIn.objects.filter(activityNum=activityNum).update(hasNewMessage='1')
            mes = ActivityMessage()
            mes.activityNum = activityNum
            mes.messageContent = request.POST.get("messageContent")
            mes.save()
            res = {'content': 'successfully send'}
            response = HttpResponse(json.dumps(res))
            return response
        except:
            res = {"error": "no such openID"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def get_message_list(request):  # 小程序端读取消息，一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            isDetail = request.POST.get('isDetail')
            openID = request.POST.get('openID')
            pageNum = request.POST.get('pageNum')
            pageNum = int(pageNum)
            pageNum -= 1
            objActiList = TakePartIn.objects.filter(openID=openID)  # 选出该用户参加过的活动
            # print(len(objActiList))
            activityList = []
            for i in objActiList:
                tempList = objActiList.filter(activityNum=i.activityNum)  # 对于每个参加了的活动
                if len(tempList) != 1:
                    res = {"error": "wrong"}
                    return HttpResponse(content=json.dumps(res), status=200)
                try:
                    activity = ActivityInfo.objects.get(activityNum=tempList[0].activityNum)
                except:
                    res = {"error": "no such activity"}
                    return HttpResponse(content=json.dumps(res), status=200)
                try:
                    activity2 = ActivityMessage.objects.filter(activityNum=tempList[0].activityNum)[0]  # 第一条消息
                except:
                    res = {"error": "no such activity"}
                    return HttpResponse(content=json.dumps(res), status=200)
                hasNewMes = tempList[0].hasNewMessage
                temp = {'num': tempList[0].activityNum, 'name': activity.activityName,
                        'content': activity2.messageContent,
                        'time': activity2.createTime.strftime("%Y-%m-%d %H:%M:%S"), 'hasNewMes': hasNewMes}
                activityList.append(temp)
            activityList.sort(key=lambda x: x['time'], reverse=True)
            print(activityList)
            if isDetail == 'True':
                page = len(activityList)//7 + 1
                resList = activityList[pageNum * 7:pageNum * 7 + 7]
                res = {'content': resList, 'page': page}
                response = HttpResponse(json.dumps(res))
                return response
            elif isDetail == 'False':
                resList = activityList[0:3]
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
def get_detail_message(request):
    if request.method == 'POST':
        try:
            # openID = request.POST.get('openID')
            activityNum = request.POST.get("activityNum")
            pageNum = request.POST.get('pageNum')
            pageNum = int(pageNum)
            pageNum -= 1
            objMsgList = ActivityMessage.objects.filter(activityNum=activityNum).order_by('-createTime')
            try:
                activity = ActivityInfo.objects.get(activityNum=activityNum)
            except:
                res = {"error": "no such activity"}
                return HttpResponse(content=json.dumps(res), status=200)
            msgList = []
            for i in objMsgList:
                temp = {'content': i.messageContent, 'time': i.createTime.strftime("%Y-%m-%d %H:%M:%S")}
                msgList.append(temp)
            resList = msgList[pageNum * 5:pageNum * 5 + 5]
            res = {'name': activity.activityName, 'content': resList}
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
            openid = request.POST.get("openID")
            takepartin = TakePartIn.objects.filter(openID=openid)
            if len(takepartin) > 0:
                for i in takepartin:
                    if i.activityNum == activityNum:
                        res = {'wrong': 'already joined in'}
                        response = HttpResponse(json.dumps(res), status=200)
                        return response
            try:
                activity = ActivityInfo.objects.get(activityNum=activityNum)
            except:
                res = {'wrong': 'activity does not exist'}
                response = HttpResponse(json.dumps(res), status=200)
                return response
            # if activity.peopleNeed == activity.peopleCurrent:
            #     res = {'wrong': 'activity is full'}
            #     response = HttpResponse(json.dumps(res), status=200)
            #     return response
            member = TakePartIn()
            member.activityNum = activityNum
            member.openID = openid
            member.save()
            temp = activity.peopleCurrent
            temp += 1
            ActivityInfo.objects.filter(activityNum=activityNum).update(peopleCurrent=temp)
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
def join_group(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            groupid = request.POST.get("groupID")
            openid = request.POST.get("openID")
            try:
                users = GroupMember.objects.get(openID=openid)
                res = {'wrong': 'already joined in'}
                response = HttpResponse(json.dumps(res), status=200)
                return response
            except:
                member = GroupMember()
                member.groupID = groupid
                member.userID = openid
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
def send_group_info(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            groupID = request.POST.get('groupID')
            try:
                group = GroupInfo.objects.get(groupID=groupID)
            except:
                res = {"error": "group does not exist"}
                return HttpResponse(content=json.dumps(res), status=200)
            res = {"groupID": group.groupID, "groupName": group.groupName,
                   "groupIntro": group.groupIntro, "groupHead": group.groupHead}
            return HttpResponse(content=json.dumps(res), status=200)
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


def gen_activityNum():
    onumList = ActivityInfo.objects.filter()
    if len(onumList) == 0:
        return 10000
    numList = []
    for i in onumList:
        numList.append(int(i.activityNum))
    numList.sort()
    activityNum = numList[-1] + 1
    return activityNum


@csrf_exempt
def create_activity(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            activity = ActivityInfo()
            activity.activityName = request.POST.get('activityName')
            activity.activityNum = gen_activityNum()
            activity.peopleNeed = request.POST.get('peopleNeed')
            activity.activityOwner = request.POST.get('activityOwner')
            activity.activityScore = request.POST.get('activityScore')
            activity.activityDescribe = request.POST.get('activityDescribe')
            activity.activityPoster = request.FILES.get('photo')
            #activity.activityAddress = request.POST.get('address')
            #activity.activityType = request.POST.get('type')
            #activity.activityContact = request.FILES.get('scanCode')
            activity.startDate = request.POST.get('start_date')
            activity.endDate = request.POST.get('end_date')
            activity.activityStatus = '-1'
            qrcode = hashlib.md5(str(activity.activityNum).encode()).hexdigest()
            activity.signInQrcode = 'i' + qrcode
            activity.signOffQrcode = 'o' + qrcode
            activity.save()
            res = {"activity_created": "1"}
            return HttpResponse(content=json.dumps(res), status=200)
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=200)


def gen_groupID():
    onumList = GroupInfo.objects.filter()
    if len(onumList) == 0:
        return 10000
    numList = []
    for i in onumList:
        numList.append(int(i.groupID))
    numList.sort()
    groupID = numList[-1] + 1
    return groupID


@csrf_exempt
def create_group(request):  # 一个demo，需要后续修改与debug
    if request.method == 'POST':
        try:
            group = GroupInfo()
            group.groupName = request.POST.get('groupName')
            group.groupID = str(gen_groupID())
            group.save()
            res = {"group_created": "1"}
            return HttpResponse(content=json.dumps(res), status=200)
        except:
            res = {"error": "wrong"}
            return HttpResponse(content=json.dumps(res), status=200)
    else:
        res = {"error": "wrong method"}
        return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def wechat_signin(request):
    if request.method == 'POST':
        try:
            qrcode = request.POST.get("qrcode")
            openid = request.POST.get("openID")
            users = models.UserInfo.objects.filter(openID=openid)
            if len(users) == 0:
                res = {"error": "no valid user"}
                return HttpResponse(json.dumps(res))
            if qrcode is None:
                res = {"error": "no valid qrcode"}
                return HttpResponse(json.dumps(res))
            #签到
            if qrcode[0] == 'i':
                activity = models.ActivityInfo.objects.filter(signInQrcode=qrcode)
                if len(activity) == 0:
                    res = {"error": "no valid qrcode"}
                    return HttpResponse(json.dumps(res))
                takepartin = models.TakePartIn.objects.filter(activityNum=activity[0].activityNum, openID=openid)
                if len(takepartin) == 0:
                    res = {"error": "have not take part in"}
                    return HttpResponse(json.dumps(res))
                #todo
                print(takepartin[0].startTime)
                if takepartin[0].startTime != '':
                    res = {"error": "have already signed in"}
                    return HttpResponse(json.dumps(res))
                starttime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
                takepartin[0].startTime = starttime
                takepartin[0].save()
                res = {'1': 'succeed'}
                return HttpResponse(json.dumps(res))

            if qrcode[0] == 'o':
                activity = models.ActivityInfo.objects.filter(signOffQrcode=qrcode)
                if len(activity) == 0:
                    res = {"error": "no valid qrcode"}
                    return HttpResponse(json.dumps(res))
                takepartin = models.TakePartIn.objects.filter(activityNum=activity[0].activityNum, openID=openid)
                if len(takepartin) == 0:
                    res = {"error": "have not take part in"}
                    return HttpResponse(json.dumps(res))
                if takepartin[0].startTime == '':
                    res = {"error": "have not signed in"}
                    return HttpResponse(json.dumps(res))
                if takepartin[0].endTime != '':
                    res = {"error": "have already signed off"}
                    return HttpResponse(json.dumps(res))
                endtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
                takepartin[0].endTime = endtime
                takepartin[0].save()
                res = {'1': 'succeed'}
                return HttpResponse(json.dumps(res))

            res = {"error": "no valid qrcode"}
            return HttpResponse(json.dumps(res))

        except:
            res = {"error": "wrong"}
            return HttpResponse(json.dumps(res), status=400)
    else:
        res = {"error": "wrong"}
        return HttpResponse(content=json.dumps(res), status=400)


#校团委登录
@csrf_exempt
def CCYL_login(request):
    if request.method == 'POST':
        username = request.POST.get("userID")
        password = request.POST.get("password")
        user = Administrator.objects.filter(username=username)
        if len(user) == 0:
            res = [{"messege": "no such user"}]
            return HttpResponse(json.dumps(res))
        password = hashlib.md5(password.encode()).hexdigest()
        if user[0].password != password:
            res = [{"messege": "wrong password"}]
            return HttpResponse(json.dumps(res))
        session = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        Administrator.objects.filter(username=username).update(sessionID=session)
        res = HttpResponse(json.dumps([{"messege": "succeed"}]))
        res["Set-Cookie"] = "session_id=" + session
        return res


@csrf_exempt
def logon(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
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


#页面跳转
@csrf_exempt
def page_render(request):
    sessionid = request.COOKIES.get("session_id")
    try:
        Administrator.objects.get(sessionID=sessionid)
        path = request.path[1:]
        try:
            return render(request, path)
        except:
            res = {"error": "wrong page"}
            return HttpResponse(json.dumps(res))
    except:
        return render(request, "CCYL_login.html")


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
            # , render_to_response('homepage.html')
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
            return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def testpass(request):
    name = request.POST.get('name')
    print(name)
    res = {"error": "require POST"}
    return HttpResponse(content=json.dumps(res), status=200)


@csrf_exempt
def export_excel(request):

    activitynum = request.POST.get('activityNum')
    activityname = request.POST.get('activityName')
    takepartin = TakePartIn.objects.filter(activityNum=activitynum)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename='+activityname+'.xls'
    """导出excel表"""
    if takepartin:
        # 创建工作簿
        ws = xlwt.Workbook(encoding='utf-8')
        # 添加第一页数据表
        w = ws.add_sheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
        # 写入表头
        w.write(0, 0, u'序号')
        w.write(0, 1, u'姓名')
        w.write(0, 2, u'学号')
        w.write(0, 3, u'工时')
        # 写入数据
        excel_row = 1
        for i in takepartin:
            student = UserInfo.objects.get(openID=i.openID)
            name = student.userName
            userid = student.userID
            manhours = i.manHours
            w.write(excel_row, 0, excel_row)
            w.write(excel_row, 1, name)
            w.write(excel_row, 2, userid)
            w.write(excel_row, 3, manhours)
            excel_row += 1
        # 写出到IO
        output = BytesIO()
        ws.save(output)
        # 重新定位到开始
        output.seek(0)
        response.write(output.getvalue())
    return response

