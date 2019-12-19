<template>
  <div>
    <div class="userInfo">
      <div class="userInfo-avatar">
        <img :src="avatarUrl" />
      </div>
      <div>{{name}}</div>
    </div>
    <div class="intro">
      <div>团体简介：</div>
      <div class="info">{{info}}</div>
    </div>
    <div class="more">
      <div v-if="followed" class="followed" @click="toUnfollow">
        <div>不再关注</div>
      </div>
      <div v-else class="unfollowed" @click="toFollow">关注</div>
      <div class="activity">组织的活动</div>
    </div>
  </div>
</template>

<script>
import config from "@/config.js";
export default {
  onShow() {
    this.source = this.$root.$mp.query.source;
    var _this = this;
    wx.request({
      url: config.getGroupDetail,
      dataType: "json",
      data: {
        groupID: _this.source,
        openID: _this.GLOBAL.openid
      },
      method: "POST",
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        if (res.statusCode == 200) {
          console.log(res);
          _this.name = res.data.groupName;
          _this.followed = res.data.followed;
          if (res.data.followed == "yes") {
            _this.followed = true;
          } else {
            _this.followed = false;
          }
          _this.info = res.data.groupIntro;
          _this.avatarUrl =
            "https://2019-a17.iterator-traits.com/media/" + res.data.groupHead;
        } else {
          console.log(res.errMsg);
        }
      }
    });
  },
  data() {
    return {
      source: "0",
      name: "",
      info: "",
      avatarUrl: "",
      followed: false
    };
  },
  methods: {
    toFollow() {
      var _this = this;
      wx.request({
        url: config.addattention,
        dataType: "json",
        data: {
          groupID: _this.source,
          openID: _this.GLOBAL.openid
        },
        method: "POST",
        header: { "content-type": "application/x-www-form-urlencoded" },
        success: function(res) {
          if (res.statusCode == 200) {
            console.log(res);
            if (res.data.success) {
              wx.showToast({
                title: "关注成功",
                icon: "",
                duration: 1500
              });
            } else {
              wx.showToast({
                title: "关注失败",
                icon: "none",
                duration: 1500
              });
            }
            _this.$mp.page.onShow();
          } else {
            console.log(res.errMsg);
          }
        }
      });
    },
    toUnfollow() {
      var _this = this;
      wx.request({
        url: config.disattention,
        dataType: "json",
        data: {
          groupID: _this.source,
          openID: _this.GLOBAL.openid
        },
        method: "POST",
        header: { "content-type": "application/x-www-form-urlencoded" },
        success: function(res) {
          if (res.statusCode == 200) {
            console.log(res);
            if (res.data.success) {
              wx.showToast({
                title: "取关成功",
                icon: "",
                duration: 1500
              });
            } else {
              wx.showToast({
                title: "取关失败",
                icon: "none",
                duration: 1500
              });
            }
            _this.$mp.page.onShow();
          } else {
            console.log(res.errMsg);
          }
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

.userInfo-avatar img {
  overflow: hidden;
  display: block;
  width: 160rpx;
  height: 160rpx;
  border-radius: 50%;
}

.intro {
  margin: 40rpx;
  font-size: 40rpx;
  /* border: 2px solid rgb(202, 77, 77); */
  color: rgb(122, 114, 189);
}

.info {
  margin: 20rpx;
  font-size: 30rpx;
}

.more {
  display: flex;
  flex-direction: row;
  margin: 80rpx;
  font-size: 40rpx;
  /* border: 2px solid rgb(202, 77, 77); */
  justify-content: space-between;
  align-items: center;
}

.followed {
  display: flex;
  flex-direction: row;
  height: 70rpx;
  width: 180rpx;
  color: #fff;
  background-color: rgb(122, 114, 189);
  align-items: center;
  justify-content: center;
}

.unfollowed {
  display: flex;
  flex-direction: row;
  height: 70rpx;
  width: 180rpx;
  color: #fff;
  background-color: rgb(122, 114, 189);
  align-items: center;
  justify-content: center;
}
.activity {
  display: flex;
  flex-direction: row;
  height: 70rpx;
  width: 240rpx;
  color: #fff;
  background-color: rgb(122, 114, 189);
  align-items: center;
  justify-content: center;
}
</style>