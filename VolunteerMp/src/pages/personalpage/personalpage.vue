<template>
  <div>
    <div class="userInfo">
      <div class="userInfo-1">
        <div class="userInfo-detail" v-if="ifLegalize" style="color:rgb(255,255,255)">></div>
        <div class="userInfo-detail" v-else style="color:rgb(255,255,255)">></div>
        <div class="userInfo-avatar">
          <open-data type="userAvatarUrl"></open-data>
        </div>
        <img class="userInfo-detail" v-if="ifLegalize" @click="toUserInfo" src="../../../static/images/toinfo.png" alt="活动图标" />
        <div class="userInfo-detail" v-else style="color:rgb(255,255,255)">></div>
      </div>
      <open-data type="userNickName"></open-data>
      <div v-if="ifLegalize"></div>
      <div class="logon" v-else @click="toLogon">身份验证</div>
    </div>

    <div class="userAction" v-if="ifLegalize">
      <div class="userActive" @click="toPersonalActive">
        <img class="userActiveImg" src="../../../static/images/activity.png" alt="活动图标" />
        <div class="userActiveDiv">我的活动</div>
      </div>
      <div>
        <div>—————————————————</div>
      </div>
      <div class="userActive" @click="toScan">
        <img class="userActiveImg" src="../../../static/images/Qrcode.png" alt="活动图标" />
        <div class="userActiveDiv">扫码签到</div>
      </div>
      <div>
        <div>—————————————————</div>
      </div>
      <div class="userActive" @click="toPersonalcertificate">
        <img class="userActiveImg" src="../../../static/images/award.png" alt="活动图标" />
        <div class="userActiveDiv">我的志愿</div>
      </div>
      <div>
        <div>—————————————————</div>
      </div>
      <div class="userActive" @click="toPersonalattenrion">
        <img class="userActiveImg" src="../../../static/images/attention.png" alt="活动图标" />
        <div class="userActiveDiv">我的关注</div>
      </div>
    </div>
    <div v-else></div>
  </div>
</template>

<script>
import qcloud from "wafer2-client-sdk";
import config from "@/config.js";

var openid = 0;
var ifLegalize = false;
var __this;
function Equal(p1, p2) {
  p1 = p2;
}
App({
  onShow: function(options) {
    var extraData = null;
    var _this = this;
    _this.openid = openid;
    if (options) {
      if (options.referrerInfo.extraData) {
        extraData = options.referrerInfo.extraData;
        _this.token = extraData.token;
        console.log(_this.token);
        wx.request({
          url: config.identity,
          dataType: "json",
          data: {
            token: _this.token,
            openid: _this.openid
          },
          method: "POST",
          header: { "content-type": "application/x-www-form-urlencoded" },
          success: function(res) {
            if (res.statusCode == 200) {
              if (res.data.error.message == "success") {
                ifLegalize = true;
                console.log(ifLegalize);
                __this.GLOBAL.ifLegalize = true;
                wx.navigateTo({ url: "../userInfo/main" });
              }
              console.log(res);
            } else {
              console.log(res.errMsg);
            }
            console.log(res);
          }
        });
      }
    }
  }
});

export default {
  created() {
    console.log("personalpage ready");
  },

  onShow() {
    console.log(this);
    this.ifLegalize = ifLegalize;
    this.GLOBAL.ifLegalize = ifLegalize;
  },

  mounted() {
    __this = this;
    var _this = this;
    ifLegalize = this.GLOBAL.ifLegalize;
    wx.login({
      success: function(res) {
        console.log(res);
        wx.request({
          url: config.loginUrl,
          dataType: "json",
          data: {
            code: res.code
          },
          method: "POST",
          header: { "content-type": "application/x-www-form-urlencoded" },
          success: function(res) {
            if (res.statusCode == 200) {
              if (res.data.error) {
                console.log(res.data.error);
                _this.GLOBAL.ifLegalize = false;
              } else {
                _this.GLOBAL.ifLegalize = true;
                ifLegalize = true;
                _this.$mp.page.onShow();
              }
              _this.GLOBAL.openid = res.data.openid;
              openid = _this.GLOBAL.openid;
              console.log(res);
            } else {
              console.log(res.errMsg);
            }
          }
        });
      }
    });
  },

  data() {
    return {
      ifLegalize: this.GLOBAL.ifLegalize
    };
  },
  methods: {
    toUserInfo() {
      //console.log("userInfo clicked")
      wx.navigateTo({ url: "../userInfo/main" });
    },
    toPersonalActive() {
      //console.log("personalactive clicked")
      wx.navigateTo({ url: "../personalactive/main" });
    },
    toPersonalcertificate() {
      //console.log("personalcertificate clicked")
      wx.navigateTo({ url: "../personalcertificate/main" });
    },
    toScan() {
      wx.navigateTo({ url: "../scanpage/main" });
    },
    toPersonalattenrion() {
      wx.navigateTo({ url: "../personalattention/main" });
    },
    toLogon() {
      wx.navigateToMiniProgram({
        appId: "wx1ebe3b2266f4afe0",
        path: "pages/index/index",
        envVersion: "trial",
        extraData: {
          origin: "miniapp",
          type: "id.tsinghua"
        },
        success(res) {
          console.log("yes");
          // 打开成功
        },
        fail(res) {
          console.log("failed");
        }
      });
    },
    changeValue() {}
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
  justify-content: space-between;
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

.userInfo-detail {
  font-size: 90rpx;
  height: 120rpx;
  width: 120rpx;
  /* border: 2px solid rgb(202, 77, 77); */
}

.userAction {
  color: rgb(122, 114, 189);
  padding: 15rpx;
}

.userActive {
  display: flex;
  height: 70rpx;
  flex-direction: row;
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

.logon {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 90rpx;
  width: 300rpx;
  margin-top: 30rpx;
  font-size: 50rpx;
  color: #fff;
  background-color: rgb(122, 114, 189);
}
</style>