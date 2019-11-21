<template>
    <div>
        <div class="userInfo">
            <div class="userInfo-1">
                <div class="userInfo-detail" v-if="ifLegalize" style="color:rgb(255,255,255)"> > </div>
                <div class="userInfo-detail" v-else style="color:rgb(255,255,255)"> > </div>
                <div class="userInfo-avatar">
                    <open-data  type="userAvatarUrl"></open-data>    
                </div>
                <div class="userInfo-detail" v-if="ifLegalize" @click="toUserInfo"> > </div>
                <div class="userInfo-detail" v-else style="color:rgb(255,255,255)"> > </div>
            </div>
            <open-data type="userNickName"></open-data>    
        </div>
        <div class="userAction" v-if="ifLegalize">
            <div class="userActive" @click="toPersonalActive">
                <img class="userActiveImg" src="../../../static/images/tabbar_personalpage.png" alt="活动图标">
                <div class="userActiveDiv">我的活动</div>
            </div>
            <div>
                <div>————这是分割线—————</div>
            </div>
             <div class="userActive" @click="toPersonalcertificate">
                <img class="userActiveImg" src="../../../static/images/tabbar_personalpage.png" alt="活动图标">
                <div class="userActiveDiv">我的证书</div>
            </div>
            <div>
                <div>————这是分割线—————</div>
            </div>
            <div class="userActive">
                <img class="userActiveImg" src="../../../static/images/tabbar_personalpage.png" alt="活动图标">
                <div class="userActiveDiv">我的关注</div>
            </div>
        </div>
        <div v-else>

        </div>
        

    </div>
</template>

<script>
import qcloud from 'wafer2-client-sdk'
import config from '@/config.js'
export default {

    created() {
        console.log('personalpage ready')
    },

    mounted() {
        wx.login({
            success: function (res) {
              console.log(res)
              wx.request({
                url:config.loginUrl,
                dataType: "json",
                data: {
                    code: res.code,
                },
                method: 'POST',
                header: { 'content-type': 'application/x-www-form-urlencoded'},
                success: function (res) {
                 if (res.statusCode == 200) {
                     if(res.data.error)
                     {
                         console.log(res.data.error);
                     }
                     else{
                        console.log(res.data.openid);
                     }
                 }
                 else {
                   console.log(res.errMsg)
                 }
              },
            })
          }
        })
    },

    data() {
        return {
            ifLegalize:true,
        }
    },
    methods: {
        toUserInfo(){
            //console.log("userInfo clicked")
            wx.navigateTo({url: '../userInfo/main'})
        },
        toPersonalActive () {
            //console.log("personalactive clicked")
            wx.navigateTo({url: '../personalactive/main'})
        },
        toPersonalcertificate(){
            //console.log("personalcertificate clicked")
            wx.navigateTo({url: '../personalcertificate/main'})
        },
    }
}
</script>

<style>
.userInfo {  
  position: relative;    
  color: rgb(122, 114, 189);  
  display:flex;  
  flex-direction:column;  
  align-items: center;  
}

.userInfo-1{
    display: flex;  
    flex-direction:row;
    width: 460rpx;  
    height: 230rpx;  
    /* border: 2px solid rgb(202, 77, 77); */
    justify-content:space-between;
    align-items: center;
}

.userInfo-avatar {  
  overflow:hidden;  
  display: block;  
  width: 160rpx;  
  height: 160rpx;  
  margin: 20rpx;  
  margin-top: 50rpx;  
  border-radius: 50%;  
  border: 2px solid #fff;  
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
     
}

.userInfo-detail{
    font-size:90rpx;
    width: 90rpx;
    /* border: 2px solid rgb(202, 77, 77); */
}

.userAction{
    color: rgb(122, 114, 189);
    padding: 15rpx  
}

.userActive{
    display: flex;
    height: 70rpx;
    flex-direction:row;
}

.userActiveImg{
    width: 70rpx;
    height: 100%;

}

.userActiveDiv{
    font-size:40rpx;
    text-indent: 30rpx;
    text-align: center;
    line-height: 70rpx;
    
}

</style>