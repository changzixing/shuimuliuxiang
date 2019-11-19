from django.conf.urls import url
from . import views

urlpatterns = [
    url('wechat_logon, views.logon'),
    url('logon', views.logon),
    url('login', views.login),
]