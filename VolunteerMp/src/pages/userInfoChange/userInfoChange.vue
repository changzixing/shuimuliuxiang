<template>
  <div class="userInfo">
    <div class="userInfo-data">
      <div>姓名：{{name}}</div>
      <div>学号：{{studentId}}</div>
      <div>院系：{{school}}</div>
      <div class="userInfo-change">
        <div>性别：</div>
        <picker
          @change="bindPickerChange"
          :value="sex"
          :range="sex_arr">
          <view class="picker">
            <div>{{sex}}</div>
            <img class="pull" src="../../../static/images/pull.png" alt="活动图标" />
          </view>
        </picker>
      </div>
      <div class="userInfo-change">
        <div style="font-size:30rpx">志愿北京编号：</div>
        <input type="text" v-model="volunteerId" />
      </div>
      <div class="userInfo-change">
        <div>联系电话：</div>
        <input type="text" v-model="phoneNumber" />
      </div>
      <div class="userInfo-change">
        <div>联系邮箱：</div>
        <input type="text" v-model="email" />
      </div>
      <div class="userInfo-change">
        <div>公益兴趣：</div>
        <input type="text" v-model="interest" />
      </div>
      <div class="userInfo-change">简介：</div>
      <div class="userInfo-change-intro">
        <input type="text" v-model="introduction" />
      </div>
    </div>

    <button class="userInfo-changeDone" @click="changeInfo">提交修改</button>
  </div>
</template>

<script>
import config from "@/config.js";
export default {
  data() {
    return {
      name: "张三",
      studentId: "2014000000",
      school: "xx系",
      sex: "1",
      volunteerId: "1",
      phoneNumber: "1",
      email: "1",
      interest: "1",
      introduction: "还没有简介哦",
      sex_arr:["男","女"]
    };
  },

  mounted() {
    var _this = this;
    wx.request({
      url: config.userInfo,
      dataType: "json",
      data: {
        openID: _this.GLOBAL.openid
      },
      method: "POST",
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        if (res.statusCode == 200) {
          if (res.data.error) {
          } else {
            _this.name = res.data.name;
            _this.studentId = res.data.studentId;
            _this.school = res.data.department;

            _this.sex = res.data.sex;
            _this.volunteerId = res.data.volunteerId;
            _this.phoneNumber = res.data.phoneNumber;
            _this.email = res.data.email;
            _this.interest = res.data.interest;
            _this.introduction = res.data.introduction;
          }
        } else {
          console.log(res.errMsg);
        }
        console.log(res);
      }
    });
  },

  methods: {
    bindPickerChange(e){
      this.sex = this.sex_arr[e.mp.detail.value];
    },
    changeInfo() {
      var _this = this;
      wx.request({
        url: config.userInfoChange,
        dataType: "json",
        data: {
          openID: _this.GLOBAL.openid,
          sex: _this.sex,
          volunteerId: _this.volunteerId,
          phoneNumber: _this.phoneNumber,
          email: _this.email,
          interest: _this.interest,
          introduction: _this.introduction
        },
        method: "POST",
        header: { "content-type": "application/x-www-form-urlencoded" },
        success: function(res) {
          if (res.statusCode == 200) {
            if (res.data.result) {
              wx.showToast({
                title: "修改成功",
                icon: "",
                duration: 2000
              });
              wx.navigateBack({});
            } else {
              wx.showToast({
                title: "修改失败，请重试",
                icon: "none",
                duration: 2000
              });
            }
          } else {
            wx.showToast({
              title: "修改失败，请重试",
              icon: "none",
              duration: 2000
            });
            console.log(res.errMsg);
          }
          console.log(res);
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

.userInfo-data {
  width: 600rpx;
  line-height: 60rpx;
  margin-top: 30rpx;
  font-size: 35rpx;
  /* border: 2px solid rgb(180, 109, 109); */
}

.userInfo-change {
  display: flex;
  flex-direction: row;
  width: 600rpx;
  align-items: center;

  /* border: 2px solid rgb(180, 109, 109); */
}

.userInfo-change input {
  border: 2px solid rgba(59, 56, 59, 0.459);
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}

.userInfo-change-intro {
  width: 500rpx;
  height: 300rpx;
  margin-left: 50rpx;
  line-height: 40rpx;
  font-size: 30rpx;
  margin-top: 5rpx;
  border: 2px solid rgba(59, 56, 59, 0.459);
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}

.userInfo-changeDone {
  flex-direction: column;
  height: 90rpx;
  width: 300rpx;
  margin-top: 30rpx;
  font-size: 50rpx;
  color: #fff;
  background-color: rgb(122, 114, 189);
  display: flex;
  justify-content: center;
  align-items: center;
}

.picker{
  border: 2px solid rgba(59, 56, 59, 0.459);
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
  height: 60rpx;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-items: center;
}

.picker div{
  width: 100rpx;
}

.pull{
  height: 40rpx;
  width: 40rpx;
  margin: 10rpx,60rpx;
  align-items: center;
  justify-items: center;
}
</style>