<template>
  <div>
    <div v-if="ifshow">
      <div class="moreMessage">
        <div>更多消息</div>
        <img @click="toMoreMessage" src="../../../static/images/toinfo.png" alt="活动图标" />
      </div>
      <div v-for="message in messages" :key="message.id" @click="toMessageShow(message.num)">
        <Messagebox :message="message"></Messagebox>
      </div>
    </div>
    <div v-else class="not">请先登录</div>
  </div>
</template>

<script>
import Messagebox from "@/components/messageBox"
import config from '@/config.js'
export default {
    
    onShow(){
        var _this = this;
        wx.request({
            url:config.messageList,
            dataType: "json",
            data: {
                openID:_this.GLOBAL.openid,
                pageNum:1,
                isDetail:"False"
            },
            method: 'POST',
            header: { 'content-type': 'application/x-www-form-urlencoded'},
            success: function (res) {
                if (res.statusCode == 200) {
                    console.log(res);
                    _this.messages = res.data.content;
                }
                else {
                   console.log(res.errMsg);
                }
            },
        })
    },
    mounted() {
        this.ifshow = this.GLOBAL.ifLegalize;
    },
    components:{
        Messagebox
    },
    data(){
        return{
            messages:[
            ],
            ifshow: false,
        }
    },
    methods: {
        toMoreMessage(){
            wx.navigateTo({url: '../messageDetails/main'})
        },
        toMessageShow(source){
            wx.navigateTo({url: '../messageShow/main?source='+source})
        }
    },
}
</script>

<style>
Messagebox{
  margin: 30rpx;
}

.moreMessage {
  display: flex;
  flex-direction: row;
  height: 70rpx;
  font-size: 40rpx;
  /* border: 2px solid rgb(202, 77, 77); */
  justify-content: space-between;
  align-items: center;
  margin: 20rpx;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.moreMessage img{
    height: 70rpx;
    width: 70rpx;
}

.not{
    font-size: 100rpx;
}
</style>