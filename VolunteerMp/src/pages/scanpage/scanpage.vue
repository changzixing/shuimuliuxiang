<template>
  <div>
    <div class="userInfo">
      <div class="userInfo-1">
        <div class="userInfo-avatar">
          <open-data type="userAvatarUrl"></open-data>
        </div>
      </div>
      <open-data type="userNickName"></open-data>
    </div>
    <button @click="scanQR">点此扫码</button>
  </div>
</template>

<script>
import config from "@/config.js";
export default {
  methods: {
    scanQR() {
      var _this = this;
      wx.scanCode({
        onlyFromCamera: true,
        success(res) {
          console.log(res);
          wx.request({
            url: config.scanQRcode,
            dataType: "json",
            data: {
              qrcode: res.result,
              openID: _this.GLOBAL.openid
            },
            method: "POST",
            header: { "content-type": "application/x-www-form-urlencoded" },
            success: function(res) {
              if (res.statusCode == 200) {
                if (res.data.error) {
                  if (res.data.error == "have not take part in") {
                    wx.showToast({
                      title: "请先参加活动",
                      icon: "none",
                      duration: 2000
                    });
                  }
                  else if (res.data.error == "have already signed in") {
                    wx.showToast({
                      title: "您已签到",
                      icon: "none",
                      duration: 2000
                    });
                  }
                  else if (res.data.error == "have already signed off") {
                    wx.showToast({
                      title: "您已签退",
                      icon: "none",
                      duration: 2000
                    });
                  }
                  else{
                    wx.showToast({
                      title: "扫码失败",
                      icon: "none",
                      duration: 2000
                    });
                  }
                } else {
                  if(res.data.success == "signin"){
                    wx.showToast({
                      title: "签到成功",
                      icon: "",
                      duration: 2000
                    });
                  }
                  else if(res.data.success == "signoff"){
                     wx.showToast({
                      title: "签退成功",
                      icon: "",
                      duration: 2000
                    });
                  }
                }
              } else {
                console.log(res.errMsg);
              }
              console.log(res);
            }
          });
        }
      });
    }
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

button {
  height: 100rpx;
  position: relative;
  color: rgb(122, 114, 189);
  display: flex;
  margin: 50rpx;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>