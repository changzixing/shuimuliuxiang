<template>
  <div class="All">
    <div class="userInfo">
      <div class="userInfo-1">
        <div class="userInfo-avatar">
          <open-data type="userAvatarUrl"></open-data>
        </div>
      </div>
      <open-data type="userNickName"></open-data>
    </div>
    <div class="timeShow">
        <div class="ShowRow">
            <div class="ShowNumber">{{volunteerTime}}</div>
            <div class="ShowChar">志愿时长</div>
        </div>
        <div class="ShowRow">
            <div class="ShowNumber">{{activityNumber}}</div>
            <div class="ShowChar">参与活动</div>
        </div>
    </div>
    <div class="userActive" @click="toRankPage">
        <img class="userActiveImg" src="../../../static/images/honor.png" alt="活动图标" />
        <div class="userActiveDiv">我的排名</div>
    </div>
    <div class="userActive">
        <img class="userActiveImg" src="../../../static/images/book.png" alt="活动图标" />
        <div class="userActiveDiv">我的证书</div>
    </div>
  </div>
</template>

<script>
import config from '@/config.js'
export default {
    data() {
        return {
            volunteerTime: 12,
            activityNumber:1
        }
    },
    methods: {
      toRankPage(){
        wx.navigateTo({ url: '../rankpage/main' });
      }
    },
    onShow(){
      var _this = this;
       wx.request({
          url: config.userInfo,
          dataType: "json",
          data: {
            openID : _this.GLOBAL.openid
          },
          method: "POST",
          header: { "content-type": "application/x-www-form-urlencoded" },
          success: function(res) {
            if (res.statusCode == 200) {
              _this.volunteerTime = res.data.userScore;
              _this.activityNumber = res.data.count;
              console.log(res);
            } else {
              console.log(res.errMsg);
            }
          }
        });
    }
};
</script>

<style>
.userInfo {
  position: relative;
  color: rgb(122, 114, 189);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.userInfo-1 {
  display: flex;
  flex-direction: row;
  width: 460rpx;
  height: 230rpx;
  /* border: 2px solid rgb(202, 77, 77); */
  justify-content: center;
  align-items: center;
}

.userInfo-avatar {
  overflow: hidden;
  display: block;
  width: 160rpx;
  height: 160rpx;
  margin: 20rpx;
  margin-top: 50rpx;
  border-radius: 50%;
  border: 2px solid #fff;
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
}

.timeShow{
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    margin: 40rpx;
    width: 500rpx;
}

.ShowRow{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.ShowNumber{
    font-size: 50rpx;
    justify-content: center;
    align-items: center;
}

.ShowChar{
    font-size: 40rpx;
    justify-content: center;
    align-items: center;
    margin: 20rpx;
    color: rgb(56, 49, 122);
}

.All{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.userActive {
  display: flex;
  height: 70rpx;
  flex-direction: row;
  color: rgb(122, 114, 189);
  margin: 10rpx;
}

.userActiveImg {
  width: 70rpx;
  height: 100%;
}

.userActiveDiv {
  font-size: 40rpx;
  text-indent: 30rpx;
  text-align: center;
  line-height: 70rpx;
}
</style>