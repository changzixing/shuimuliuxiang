from django.db import models
import datetime


class UserInfo(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)  # 清华学生，学号；机构用户，另外编号
    department = models.CharField(max_length=50)
    openID = models.CharField(max_length=50)
    userScore = models.CharField(max_length=50)
    userMail = models.CharField(max_length=50)
    userPhone = models.CharField(max_length=50)
    userZhiYuanBJ = models.CharField(max_length=50)  # 志愿北京志愿者号
    hasNewMessage = models.CharField(max_length=5)


class ActivityInfo(models.Model):
    activityName = models.CharField(max_length=50)
    activityNum = models.CharField(max_length=50)
    activityOwner = models.CharField(max_length=50)
    activityScore = models.CharField(max_length=50)
    activityPoster = models.ImageField(upload_to=str("media"))
    activityDescribe = models.TextField(max_length=1000)
    startdate = models.DateField(default=datetime.date.today)
    startdate = models.DateField(default=datetime.date.today)
    activityContact = models.ImageField(upload_to=str('media')) # 上传联系人/群二维码


class TakePartIn(models.Model):
    activityNum = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)

class ActivityMeaaage(models.Model): # 记录活动与信息，每条信息对应一个活动
    activityNum = models.CharField(max_length=50)
    messageCOntent = models.TextField(max_length=1000)
# Create your models here.
