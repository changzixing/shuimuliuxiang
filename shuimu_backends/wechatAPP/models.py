import os
import uuid

from django.db import models
import datetime


def activity_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "jpeg", "png", "gif"]:
        sub_folder = "pic"
    # if ext.lower() in ["pdf", "docx"]:
    #     sub_folder = "document"
    print(instance.activityNum)
    print(sub_folder)
    print(filename)
    return os.path.join('activity', instance.activityNum, sub_folder, filename)


class UserInfo(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)  # 清华学生，学号；机构用户，另外编号
    userSex = models.CharField(max_length=10)
    department = models.CharField(max_length=50, default='')
    openID = models.CharField(max_length=50)
    userScore = models.CharField(max_length=50)
    userMail = models.CharField(max_length=50)
    userPhone = models.CharField(max_length=50)
    userZhiYuanBJ = models.CharField(max_length=50)  # 志愿北京志愿者号
    userInterest = models.CharField(max_length=50)  # 用户兴趣
    userIntro = models.CharField(max_length=200)  # 用户介绍


class GroupInfo(models.Model):  # 志愿团体信息
    groupName = models.CharField(max_length=50)
    groupID = models.CharField(max_length=50)


class GroupMember(models.Model):  # 志愿团体成员
    groupID = models.CharField(max_length=50)
    openID = models.CharField(max_length=50)


class ActivityInfo(models.Model):
    activityName = models.CharField(max_length=50)
    activityNum = models.CharField(max_length=50)
    activityOwner = models.CharField(max_length=50)
    activityScore = models.CharField(max_length=50)
    peopleNeed = models.IntegerField(default=0)
    peopleCurrent = models.IntegerField(default=0)
    activityPoster = models.ImageField(upload_to=activity_directory_path, default=0)
    activityAddress = models.CharField(max_length=100, default='')
    activityDescribe = models.TextField(max_length=1000)
    activityType = models.CharField(max_length=5, default='0')
    # activityType: 0.其他，1.文教，2.赛会，3.社区，4.医疗，5.健康
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today)
    activityContact = models.ImageField(upload_to=activity_directory_path, default=0)  # 上传联系人/群二维码
    activityStatus = models.CharField(max_length=50, default='')  # 活动状态：已结束/报名中/进行中/未开始等


class TakePartIn(models.Model):
    activityNum = models.CharField(max_length=50)
    openID = models.CharField(max_length=50)
    hasNewMessage = models.CharField(max_length=5, default='0')


class ActivityMessage(models.Model):  # 记录活动与信息，每条信息对应一个活动
    activityNum = models.CharField(max_length=50)
    createTime = models.DateTimeField(auto_now=True)
    messageContent = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-createTime']
# Create your models here.


# Create your models here.
