<template>
    <view class="activityBox">
        <view class="activityRow">
            <view class="type">
                <text v-if="activity.type=='0'">文化教育</text>
                <text v-else-if="activity.type=='1'">赛会服务</text>
                <text v-else-if="activity.type=='2'">社区服务</text>
                <text v-else-if="activity.type=='3'">医疗卫生</text>
                <text v-else-if="activity.type=='4'">健康残障</text>
                <text v-else>其他类型</text>
            </view>
            <view class="name">
                <text>{{activity.name}}</text>
            </view>
            <view class="progress">
                <text>{{activity.peopleCurrent}}/{{activity.peopleNeed}}</text>
            </view>
        </view>
        <view class="activityRow">
            <view class="location">
                <image class="icon" src="../../static/images/location.png" mode="scaleToFill"></image>
                <text>{{activity.address}}</text>
            </view>
            <view class="owner">                                
                <image class="icon" src="../../static/images/owner.png" mode="scaleToFill"></image>
                <text>{{activity.owner}}</text>
            </view>
        </view>
        <view class="activityRow">
            <view class="time">
                <image class="icon" src="../../static/images/time.png" mode="scaleToFill"></image>
                <text>{{activity.startDate}}</text>
            </view>
        </view>
    </view>
</template>

<script>
export default {
    props: ["activity"]
}
</script>

<style>
.activityBox {
    width: 600rpx;
    height: 150rpx;
    border: 2rpx solid rgb(122, 114, 189);
    border-radius: 20rpx;
    margin: 5rpx 0;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.activityRow {
    width: 590rpx;
    height: 45rpx;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.type {
    width: 130rpx;
    height: 40rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    border-radius: 10rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.name {
    width: 280rpx;
    height: 45rpx;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}

.progress {
    width: 160rpx;
    height: 45rpx;
    font-weight: bold;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
}

.location {
    width: 290rpx;
    height: 45rpx;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}

.owner {
    width: 290rpx;
    height: 45rpx;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}

.time {
    width: 580rpx;
    height: 45rpx;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}

.icon {
    width: 40rpx;
    height: 40rpx;
}
</style>