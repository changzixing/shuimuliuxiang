<template>
  <div>
    <div class="messageBlock">
      <div v-for="message in messages" :key="message.id">
        <Messageinfo :message="message"></Messageinfo>
      </div>
    </div>
    <div class="pageChange">
      <div @click="lastPage">上一页</div>
      <div>{{pageNum}} / {{pageAll}}</div>
      <div @click="nextPage">下一页</div>
    </div>
  </div>
</template>

<script>
import Messageinfo from "@/components/messageInfo";
import config from "@/config.js";
export default {
  onShow() {
    this.source = this.$root.$mp.query.source;
    console.log(this.source);
    var _this = this;
    wx.request({
      url: config.messageDetail,
      dataType: "json",
      data: {
        activityNum: _this.source,
        pageNum: 1
      },
      method: "POST",
      header: { "content-type": "application/x-www-form-urlencoded" },
      success: function(res) {
        if (res.statusCode == 200) {
          console.log(res);
          _this.messages = res.data.content;
          _this.pageAll = res.data.page;
        } else {
          console.log(res.errMsg);
        }
      }
    });
  },
  components: {
    Messageinfo
  },
  data() {
    return {
      source: "",
      messages: [],
      pageNum: 1,
      pageAll: 1
    };
  },
  methods: {
    nextPage() {
      if (this.pageNum < this.pageAll) {
        var _this = this;
        wx.request({
          url: config.messageDetail,
          dataType: "json",
          data: {
            openID: _this.GLOBAL.openid,
            pageNum: _this.pageNum + 1,
            activityNum: _this.source,
          },
          method: "POST",
          header: { "content-type": "application/x-www-form-urlencoded" },
          success: function(res) {
            if (res.statusCode == 200) {
              console.log(res);
              _this.messages = res.data.content;
              _this.pageNum += 1;
            } else {
              console.log(res.errMsg);
            }
          }
        });
      }  
    },
    lastPage() {
      if (this.pageNum !== 1) {
        var _this = this;
        wx.request({
          url: config.messageDetail,
          dataType: "json",
          data: {
            openID: _this.GLOBAL.openid,
            pageNum: _this.pageNum - 1,
            activityNum: _this.source,
          },
          method: "POST",
          header: { "content-type": "application/x-www-form-urlencoded" },
          success: function(res) {
            if (res.statusCode == 200) {
              console.log(res);
              _this.messages = res.data.content;
              _this.pageNum -= 1;
            } else {
              console.log(res.errMsg);
            }
          }
        });
      }
    }
  },
};
</script>

<style>
.messageBlock {
  height: 1250rpx;
  /* border: 2px solid rgb(202, 77, 77); */
}

.pageChange {
  position: relative;
  color: rgb(122, 114, 189);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.pageChange div {
  margin: 30rpx;
  font-size: 35rpx;
}
</style>