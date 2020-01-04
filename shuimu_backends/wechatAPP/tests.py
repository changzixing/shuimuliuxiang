from django.test import TestCase
from django.http import HttpRequest
# Create your tests here.
from . import views
import requests
# import pytest
import json

class TestClass(TestCase):

    def test_get_my_activity_0(self):
        req = HttpRequest()
        req.method = "POST"
        req.POST = {"openID": "wrongopenid", "activityStatus": "willdo", "pageNum": '1'}
        res = views.get_my_activity(req)
        assert json.loads(res.content)['error'] == 'no such user'

    # def test_get_my_activity_1(self):
    #     url = "http://localhost:8000/get_my_activity"
    #     data = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityStatus": "willdo", "pageNum": '1'}
    #     res = requests.post(url=url, data=data).json()
    #     assert res['content'] == [] or res['content']

    # def test_get_my_activity_2(self):
    #     url = "http://localhost:8000/get_my_activity"
    #     data = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityStatus": "doing", "pageNum": '1'}
    #     res = requests.post(url=url, data=data).json()
    #     assert res['content'] == [] or res['content']

    # def test_get_my_activity_3(self):
    #     url = "http://localhost:8000/get_my_activity"
    #     data = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityStatus": "done", "pageNum": '1'}
    #     res = requests.post(url=url, data=data).json()
    #     assert res['content'] == [] or res['content']

    # def test_edit_user_0(self):
    #     url = "http://localhost:8000/edit_user"
    #     data = {"openID": "wrongid"}
    #     res = requests.post(url=url, data=data).json()
    #     assert res['error'] == 'no such user'

    # def test_edit_user_1(self):
    #     url = "http://localhost:8000/edit_user"
    #     data = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "sex": "male"}
    #     res = requests.post(url=url, data=data).json()
    #     assert res['result'] == 'edit succeeded'

    # def test_send_activity_info_0(self):
    #     url = "http://localhost:8000/send_activity_info"
    #     data = {"openID": "wrongid"}
    #     res = requests.post(url=url, data=data).json()
    #     assert res['error']

    # def test_send_activity_info_1(self):
    #     url = "http://localhost:8000/send_activity_info"
    #     data = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityNum": "wrongnum"}
    #     res = requests.post(url=url, data=data).json()
    #     assert res['error']

    # def test_send_activity_info_2(self):
    #     url = "http://localhost:8000/send_activity_info"
    #     data = {"openID": "oo85p5LEN2BJ8rf1WJE0m03iM0lY", "activityNum": "10001"}
    #     res = requests.post(url=url, data=data).json()
    #    assert res['activityName']
