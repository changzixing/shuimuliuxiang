<template>
  <div>
    <div
      class="messageBlock"
      v-for="message in messages"
      :key="message.id"
      @click="toMessageShow(message.num)"
    >
      <Messagebox :message="message"></Messagebox>
    </div>
    <div class="pageChange">
      <div>上一页</div>
      <div>{{pageNum}} / {{pageAll}}</div>
      <div>下一页</div>
    </div>
  </div>
</template>

<script>
import Messagebox from "@/components/messageBox";
import config from "@/config.js";
export default {
  components: {
    Messagebox
  },
  onShow() {
    var _this = this;
    wx.request({
      url: config.messageList,
      dataType: "json",
      data: {
        openID: _this.GLOBAL.openid,
        pageNum: 1,
        isDetail: "True"
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
  data() {
    return {
      messages: [],
      pageNum: 1,
      pageAll: 1
    };
  },
  methods: {
    toMessageShow(source) {
      wx.navigateTo({ url: "../messageShow/main?source=" + source });
    },
    nextPage() {
      if (pageNum < pageAll) {
        var _this = this;
        wx.request({
          url: config.messageList,
          dataType: "json",
          data: {
            openID: _this.GLOBAL.openid,
            pageNum: _this.pageNum + 1,
            isDetail: "True"
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
      }
    },
    lastPage() {
      if (pageNum !== 1) {
        var _this = this;
        wx.request({
          url: config.messageList,
          dataType: "json",
          data: {
            openID: _this.GLOBAL.openid,
            pageNum: _this.pageNum - 1,
            isDetail: "True"
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
      }
    }
  }
};
</script>

<style>
.messageBlock {
  height: 1050rpx;
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