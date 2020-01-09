from django.test import TestCase
# Create your tests here.
from . import views
import requests
import pytest
import json
from django.test import TestCase
from django.http import HttpRequest
from wechatAPP import models
from .models import ActivityInfo, ActivityMessage
from .models import UserInfo
from .models import TakePartIn
from .models import GroupInfo
from .models import GroupMember
from .models import Administrator


class TestClass(TestCase):

    def setUp(self):
        user = UserInfo()
        user.openID = "oo85p5LEN2BJ8rf1WJE0m03iM0lY"
        user.userName = "Li"
        user.save()
        group = Administrator()
        group.groupID = 'admin'
        group.password = '123456'
        group.groupID = '000000'
        group.save()
        activity = ActivityInfo()
        activity.activityStatus = '0'
        activity.activityOwner = '000000'
        activity.activityNum = '100001'
        activity.activityScore = '10'
        activity.activityName = 'testactivity'
        activity.activityAddress = 'testaddress'
        activity.activityType = '0'
        activity.peopleNeed = 10
        activity.save()
        activity1 = ActivityInfo()
        activity1.activityStatus = '1'
        activity1.activityOwner = '000000'
        activity1.activityNum = '100002'
        activity1.activityScore = '10'
        activity1.activityName = 'testactivity1'
        activity1.activityAddress = 'testaddress1'
        activity1.activityType = '1'
        activity1.peopleNeed = 0
        activity1.save()

    def test_edit_user_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "wrongopenid"}
        res = views.edit_user(req)
        assert json.loads(res.content)['error'] == 'no such user'

    def test_send_and_edit_user_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "sex": "male"}
        views.edit_user(req)
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY"}
        res = views.send_user_info(req)
        assert json.loads(res.content)['sex'] == 'male'

    def test_send_and_edit_user_1(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "phoneNumber": "10086"}
        views.edit_user(req)
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY"}
        res = views.send_user_info(req)
        assert json.loads(res.content)['phoneNumber'] == '10086'

    def test_send_and_edit_user_2(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "phoneNumber": "10086", "sex": "male"}
        views.edit_user(req)
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY"}
        res = views.send_user_info(req)
        assert json.loads(res.content)['phoneNumber'] == '10086'
        assert json.loads(res.content)['sex'] == 'male'

    def test_join_activity_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityNum": "100001"}
        res = views.join_activity(req)
        assert json.loads(res.content)['1'] == 'succeed'

    def test_join_activity_1(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "wrongopenid", "activityNum": "100001"}
        res = views.join_activity(req)
        assert json.loads(res.content)['error'] == 'no valid user'

    def test_join_activity_2(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityNum": "000000"}
        res = views.join_activity(req)
        assert json.loads(res.content)['wrong'] == 'activity does not exist'

    def test_join_activity_3(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityNum": "100001"}
        views.join_activity(req)
        res = views.join_activity(req)
        assert json.loads(res.content)['wrong'] == 'already joined in'

    def test_join_activity_4(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityNum": "100002"}
        views.join_activity(req)
        res = views.join_activity(req)
        assert json.loads(res.content)['wrong'] == 'activity is full'

    def test_group_list_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY"}
        res = views.group_list(req)
        assert json.loads(res.content)['content']

    def test_follow_group_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "groupID": "000000"}
        views.follow_group(req)
        member = GroupMember.objects.get(groupID="000000")
        assert member.openID == "oo85p5LEN2BJ8rf1WJE0m03iM0lY"

    def test_follow_group_1(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "groupID": "100000"}
        res = views.follow_group(req)
        assert json.loads(res.content)['error'] == 'no valid group id'

    def test_follow_group_2(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "groupID": "000000"}
        views.follow_group(req)
        res = views.follow_group(req)
        assert json.loads(res.content)['error'] == 'already followed'

    def test_unfollow_group_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "groupID": "000000"}
        views.follow_group(req)
        res = views.unfollow_group(req)
        assert json.loads(res.content)['success'] == 'unfollowed'

    def test_unfollow_group_1(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "groupID": "000000"}
        res = views.unfollow_group(req)
        assert json.loads(res.content)['error'] == 'already unfollowed'

    def test_follow_list_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY"}
        res = views.follow_list(req)
        assert json.loads(res.content)['content'] == []

    def test_follow_list_1(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "groupID": "000000"}
        views.follow_group(req)
        res = views.follow_list(req)
        assert json.loads(res.content)['content'][0]['groupID'] == "000000"

    def test_send_group_info_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "groupID": "000000"}
        res = views.send_group_info(req)
        fo = open('1.txt', 'w')
        fo.write(res.content.decode())
        fo.close()
        assert json.loads(res.content)['groupID'] == '000000'

    def test_get_my_activity_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "wrongopenid", "activityStatus": "willdo", "pageNum": '1'}
        res = views.get_my_activity(req)
        assert json.loads(res.content)['error'] == 'no such user'

    def test_get_my_activity_1(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityStatus": "willdo", "pageNum": '1'}
        res = views.get_my_activity(req)
        print(res)
        assert json.loads(res.content)['content'] == [] or json.loads(res.content)['content']


