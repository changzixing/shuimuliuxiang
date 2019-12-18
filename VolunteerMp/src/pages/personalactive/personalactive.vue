<template>
    <view class="page">
        <view class="activityStatus">
            <view v-for="activityStatus in activityStatuss" :key="activityStatus.name" :class="activityStatus.picked ? 'activityStatus1' : 'activityStatus2'" @click="activityStatusChange(activityStatus)">{{activityStatus.value}}</view>
        </view>
        <view class="activityList">
            <view class="activityList" v-if="pageAll > 0">
                <activitybox v-for="activity in activities" :key="activity.id" :activity="activity"></activitybox>
            </view>
        </view>
        <view class="pageNum">
            <view @click="lastPage()">上一页</view>
            <view v-if="pageAll > 0">{{pageNum}} / {{pageAll}}</view>
            <view v-else>1 / 1</view>
            <view @click="nextPage()">下一页</view>
        </view>
    </view>
</template>

<script>
import qcloud from 'wafer2-client-sdk'
import config from '@/config.js'
import activitybox from "@/components/activityBox"
export default {
    components:{
        activitybox
    },

    created() {
        console.log("personal activity");
    },

    onShow() {
        var _this = this;
        wx.request({
            url:config.personalActivity,
            dataType: "json",
            data: {
                openID:_this.GLOBAL.openid,
                activityStatus:_this.activityStatus,
                pageNum:_this.pageNum,
            },
            method: 'POST',
            header: { 'content-type': 'application/x-www-form-urlencoded'},
            success: function (res) {
                if (res.statusCode == 200) {
                    if(res.data.error){

                    }
                    else{
                        _this.activities = res.data.content;
                        _this.pageAll = res.data.page;
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
            buttonText:"< 返回个人中心",
            activityStatus:"doing",
            activityStatuss:[
                { name: 'willdo', value: '未开始', picked: true},
                { name: 'doing', value: '进行中', picked: false},
                { name: 'done', value: '已完成', picked: false},
            ],
            pageNum: 1,
            pageAll: 1,
        }
    },

    methods: {
        activityStatusChange(activityStatus){
            var _this = this;
            for(var i in _this.activityStatuss)
            {
                _this.activityStatuss[i].picked = false;
            }
            activityStatus.picked = true;
            _this.activityStatus = activityStatus.name;
            _this.pageNum = 1;
            _this.$mp.page.onShow();
        },
        lastPage(){
            var _this = this;
            if(_this.pageAll > 0 && _this.pageNum > 1)
            {
                _this.pageNum -= 1;
                _this.$mp.page.onShow();
            }
        },
        nextPage(){
            var _this = this;
            if(_this.pageAll > 0 && _this.pageNum < _this.pageAll)
            {
                _this.pageNum += 1;
                _this.$mp.page.onShow();
            }
        },
    },
}
</script>

<style>
.page {
    width: 750rpx;
    height: 1050rpx;
    margin: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    /*border: 2rpx solid #000;*/
}

.activityStatus {
    width: 600rpx;
	height: 70rpx;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.activityList {
    width: 600rpx;
    height: 800rpx;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.pageNum {
    width: 700rpx;
    height: 60rpx;
    font-size: 35rpx;
    color: rgb(122, 114, 189);
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.activityStatus1 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.activityStatus2 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
</style>