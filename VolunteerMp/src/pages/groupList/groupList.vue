<template>
  <div>
    <div v-for="group in groups" :key="group.id" @click="toGroupShow(group.groupID)">
      <Groupbox :group="group"></Groupbox>
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
      groups: []
    };
  },
  onShow() {
    var _this = this;
    wx.request({
      url: config.grouplist,
      dataType: "json",
      data: {
        openID: _this.GLOBAL.openid
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
  methods: {
    toGroupShow(source) {
      wx.navigateTo({ url: "../groupDetail/main?source=" + source });
    }
  }
};
</script>

<style>
</style>