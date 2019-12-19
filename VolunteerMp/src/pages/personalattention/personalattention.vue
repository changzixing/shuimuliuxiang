<template>
  <div>
      <div v-for="group in groups" :key="group.id" @click="toGroupShow(group.groupID)">
        <Groupbox :group="group"></Groupbox>
      </div>
      <div class="center">
        <div class="moreGroup" @click="toMore">关注更多</div>
      </div>
  </div>
</template>

<script>
import Groupbox from "@/components/groupBox";
import config from "@/config.js";
export default {
  components: {
    Groupbox
  },
  data() {
      return {
          groups:[{name:"1",imgsrc:"../../static/images/tabbar_personalpage.png",groupID:"12"}]
      }

  },
  methods: {
      toGroupShow(source) {
        wx.navigateTo({ url: "../groupDetail/main?source=" + source });
    },
    toMore(){
      wx.navigateTo({ url: "../groupList/main"});
    }
  },
  onShow() {
    var _this = this;
    wx.request({
      url: config.myattention,
      dataType: "json",
      data: {
        openID: _this.GLOBAL.openid,
      },
      method: "POST",
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        if (res.statusCode == 200) {
          console.log(res);
          _this.groups = res.data.content;
        } else {
          console.log(res.errMsg);
        }
      }
    });
  },
};
</script>

<style>
Groupbox{
    margin: 20rpx;
}

.center{
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: center;
}

.moreGroup{
  position: relative;
  display: flex;
  flex-direction: row;
  height: 70rpx;
  width: 180rpx;
  color: #fff;
  background-color: rgb(122, 114, 189);
  align-items: center;
  justify-content: center;
  margin: 80rpx;
}
</style>