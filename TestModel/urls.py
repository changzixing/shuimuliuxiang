from django.conf.urls import url
from . import views

urlpatterns = [
    url('wechat_login', views.wechat_login),
    url('wechat_identity', views.wechat_identity),
    url('logon', views.logon),
    url('login', views.login),
    url('test', views.test),
]