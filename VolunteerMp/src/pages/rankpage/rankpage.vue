<template>
  <div>
    <div class="rankBlock">
      <Rankbox :user="text"></Rankbox>
      <div>我的排名</div>
      <Rankbox :user="myrank"></Rankbox>
      <div>排行榜</div>
      <div v-for="user in users" :key="user.id">
        <Rankbox :user="user"></Rankbox>
      </div>
    </div>
  </div>
</template>

<script>
import Rankbox from "@/components/rankBox";
import config from "@/config.js";
export default {
  components: {
    Rankbox
  },
  onShow() {
    var _this = this;
    wx.request({
      url: config.getrank,
      dataType: "json",
      data: {
        openID:_this.GLOBAL.openid
      },
      method: "POST",
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        if (res.statusCode == 200) {
            _this.users = res.data.rank;
            _this.myrank = res.data.self;
          console.log(res);
        } else {
          console.log(res.errMsg);
        }
      }
    });
  },
  data() {
    return {
      users: [],
      text: {userRank:"排名",userName:"名字",userScore:"分数"},
      myrank: {}
    };
  }
};
</script>

<style>
.rankBlock {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>