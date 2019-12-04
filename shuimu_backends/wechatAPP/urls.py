from django.conf.urls import url
from . import views

urlpatterns = [
    url('wechat_login', views.wechat_login),
    url('wechat_identity', views.wechat_identity),
    url('logon', views.logon),
    url('login', views.login),
    url('test', views.test),
    url('testhtml', views.testhtml),
    url('create_activity', views.create_activity),
    url('join_group', views.join_group),
    url('send_message', views.send_message),
    url('edit_user', views.edit_user),
    url('send_user_info', views.send_user_info),
    url('send_activity_info', views.send_activity_info),
    url('get_activity', views.get_activity),
    url('join_activity', views.join_activity),
]