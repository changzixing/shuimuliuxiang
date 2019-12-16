from .models import ActivityInfo
import time
def updata_activity():
    cur_date = time.localtime(time.time())
    activities_0 = ActivityInfo.objects.filter(activityStatus='0')      #报名中
    for activity in activities_0:
        start_date = time.strptime(activity.startDate, "%Y-%m-%d")
        if cur_date.tm_year==start_date.tm_year and cur_date.tm_mon==start_date.tm_mon and start_date.tm_mday-cur_date.tm_mday==1:
            activity.activityStatus = '1'                               #截止报名
            activity.save()

    activities_1 = ActivityInfo.objects.filter(activityStatus='1')
    for activity in activities_1:
        start_date = time.strptime(activity.startDate, "%Y-%m-%d")
        if start_date.tm_mday==cur_date.tm_mday:
            activity.activityStatus ='2'                                #活动进行中
            activity.save()

    activities_2 = ActivityInfo.objects.filter(activityStatus='2')
    for activity in activities_2:
        end_date = time.strptime(activity.endDate, "%Y-%m-%d")
        if cur_date.tm_year==end_date.tm_year and cur_date.tm_mon==end_date.tm_mon and end_date.tm_mday==cur_date.tm_mday:
            activity.activityStatus = '3'                               #活动已结束
            activity.save()



