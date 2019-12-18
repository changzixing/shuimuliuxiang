<template>
    <view class="page">
        <view class="activity1">
            <view class="type">
                <text v-if="activityType=='0'">文化教育</text>
                <text v-else-if="activityType=='1'">赛会服务</text>
                <text v-else-if="activityType=='2'">社区服务</text>
                <text v-else-if="activityType=='3'">医疗卫生</text>
                <text v-else-if="activityType=='4'">健康残障</text>
                <text v-else>其他类型</text>
            </view>
            <view class="name">{{activityName}}</view>
        </view>
        <view class="activity2">
            <image class="poster" :src="'https://2019-a17.iterator-traits.com/media/'+activityPoster" mode="aspectFit"></image>
            <view class="progress">{{peopleCurrent}}/{{peopleNeed}}</view>
        </view>
        <view class="activity3">
            <view class="text">活动主办方：{{activityOwner}}</view>
            <view class="text">活动地点：{{activityAddress}}</view>
            <view class="text">开始时间：{{startDate}}</view>
            <view class="text">结束时间：{{endDate}}</view>
            <view class="text">每小时志愿工时：{{activityScore}}</view>
        </view>
        <view class="activity4">
            <view class="text">活动简介</view>
            <view class="describe">{{activityDescribe}}</view>
        </view>
            
        <view class="signupButton" v-if="flag==0" @click="joinActivity()">我要报名</view>
        <view class="signupButton" v-else @click="quitActivity()">取消报名</view>
    </view>
</template>

<script>
import qcloud from 'wafer2-client-sdk'
import config from '@/config.js'
export default {
    created() {
        console.log('activityDetails');
    },

    onShow() {
        this.activityNum = this.$root.$mp.query.activityNum;
        console.log(this.activityNum);
        var _this = this;
        wx.request({
            url:config.activityDetails,
            dataType: "json",
            data: {
                openID:_this.GLOBAL.openid,
                activityNum:_this.activityNum,
            },
            method: 'POST',
            header: { 'content-type': 'application/x-www-form-urlencoded'},
            success: function (res) {
                if (res.statusCode == 200) {
                    if(res.data.error){

                    }
                    else{
                        _this.activityName = res.data.activityName;
                        _this.activityOwner = res.data.activityOwner;
                        _this.activityScore = res.data.activityScore;
                        _this.startDate = res.data.startDate;
                        _this.endDate = res.data.endDate;
                        _this.activityPoster = res.data.activityPoster;
                        _this.activityContact = res.data.activityContact;
                        _this.activityDescribe = res.data.activityDescribe;
                        _this.activityStatus = res.data.activityStatus;
                        _this.activityAddress = res.data.activityAddress;
                        _this.peopleNeed = res.data.peopleNeed;
                        _this.peopleCurrent = res.data.peopleCurrent;
                        _this.activityType = res.data.activityType;
                        _this.flag = res.data.flag;
                    }
                }
                else {
                    console.log(res.errMsg);
                }
                console.log(res)
            },
        })
    },

    data() {
        return {
            activityNum: "",
            activityName: "",
            activityOwner: "",
            activityScore: "",
            startDate: "",
            endDate: "",
            activityPoster: "",
            activityContact: "",
            activityDescribe: "",
            activityStatus: "",
            activityAddress: "",
            peopleNeed: 0,
            peopleCurrent: 0,
            activityType: "",
            flag: "",
        }
    },

    methods: {
        joinActivity(){
            var _this = this;
            wx.request({
                url:config.joinActivity,
                dataType: "json",
                data: {
                    openID:_this.GLOBAL.openid,
                    activityNum:_this.activityNum,
                },
                method: 'POST',
                header: { 'content-type': 'application/x-www-form-urlencoded'},
                success: function (res) {
                    if (res.statusCode == 200) {
                        if(res.data.error){

                        }
                        else{
                            wx.navigateTo({url: '../signupSuccessfully/main?activityContact='+_this.activityContact});
                        }
                    }
                    else {
                        console.log(res.errMsg);
                    }
                    console.log(res)
                },
            })
        },
        quitActivity(){
            var _this = this;
            wx.request({
                url:config.quitActivity,
                dataType: "json",
                data: {
                    openID:_this.GLOBAL.openid,
                    activityNum:_this.activityNum,
                },
                method: 'POST',
                header: { 'content-type': 'application/x-www-form-urlencoded'},
                success: function (res) {
                    if (res.statusCode == 200) {
                        if(res.data.error){

                        }
                        else{
                            _this.$mp.page.onShow();
                        }
                    }
                    else {
                        console.log(res.errMsg);
                    }
                    console.log(res)
                },
            })
        },
    },
}
</script>

<style>
.page {
    width: 750rpx;
    margin: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.activity1 {
    width: 600rpx;
    height: 55rpx;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.activity2 {
    width: 600rpx;
    height: 300rpx;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.activity3 {
    width: 600rpx;
    height: 300rpx;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.activity4 {
    width: 600rpx;
    margin: 20rpx 0;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.type {
    width: 160rpx;
    height: 50rpx;
    font-size: 35rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    border-radius: 10rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.name {
    width: 420rpx;
    height: 65rpx;
    font-size: 40rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}

.poster {
    width: 300rpx;
    height: 300rpx;
}

.progress {
    width: 280rpx;
    height: 80rpx;
    font-weight: bold;
    font-size: 50rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.text {
    width: 600rpx;
    height: 50rpx;
    font-size: 35rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}

.describe {
    width: 600rpx;
    font-size: 30rpx;
    color: #000;
    border: 2rpx solid #000;
}

.signupButton {
    width: 300rpx;
    height: 70rpx;
    font-size: 40rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    border-radius: 15rpx;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>