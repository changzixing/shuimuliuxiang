from django.db import models


class UserInfo(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)  # 清华学生，学号；机构用户，另外编号
    openID = models.CharField(max_length=50)
    userScore = models.CharField(max_length=50)
    userMail = models.CharField(max_length=50)
    userPhone = models.CharField(max_length=50)
    userZhiYuanBJ = models.CharField(max_length=50)  # 志愿北京志愿者号


class ActivityInfo(models.Model):
    activityName = models.CharField(max_length=50)
    activityNum = models.CharField(max_length=50)
    activityOwner = models.CharField(max_length=50)
    activityScore = models.CharField(max_length=50)
    activityPoster = models.ImageField(upload_to=str("img/{ID}".format(ID=str(activityNum))), default="")
    activityDescribe = models.CharField(max_length=1000)


class TakePartIn(models.Model):
    activityNum = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)
# Create your models here.
