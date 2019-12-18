<template>
    <view class="page">
        <view class="text1">报名成功！</view>
        <view class="text2">请扫二维码加入活动志愿者群</view>
        <image class="contact" :src="'https://2019-a17.iterator-traits.com/media/'+activityContact" mode="aspectFit"></image>
    </view>
</template>

<script>
import qcloud from 'wafer2-client-sdk'
import config from '@/config.js'
export default {
    created() {
        console.log('sighupSuccessfully');
    },

    onShow() {
        this.activityContact = this.$root.$mp.query.activityContact;
        console.log(this.activityContact);
    },

    data() {
        return {
            activityContact: "",
        }
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
}

.text1 {
    width: 600rpx;
    height: 100rpx;
    font-weight: bold;
    font-size: 60rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.text2 {
    width: 600rpx;
    height: 55rpx;
    font-size: 40rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.contact {
    width: 600rpx;
    height: 600rpx;
}
</style>