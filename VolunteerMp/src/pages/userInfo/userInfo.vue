<template>
    <div class="userInfo">
        <div class="userInfo-avatar">
            <open-data  type="userAvatarUrl"></open-data>    
        </div>
        <div class="userInfo-data">
            <div>姓名：{{name}}</div>
            <div>学号：{{studentId}}</div>
            <div>院系：{{school}}</div>
            <div>性别：{{sex}}</div>
            <div>志愿北京编号：{{volunteerId}}</div>
            <div>联系电话：{{phoneNumber}}</div>
            <div>联系邮箱：{{email}}</div>
            <div>公益兴趣：{{interest}}</div>
            <div>简介：</div>
            <div class="userInfo-intro">
                {{introduction}}
            </div>
        </div>
        <div class="userInfo-change" @click="toChange">
            修改信息
        </div>
    </div>
</template>

<script>
import config from '@/config.js'
export default {
    
    data() {
        return {
            name: "张三",
            studentId:"2014000000",
            school:"xx系",
            sex:"1",
            volunteerId:"1",
            phoneNumber:"1",
            email:"1",
            interest:"1",
            introduction:"还没有简介哦还没有简介哦还没有简介哦还没有简介哦还没有简介哦还没有简介哦还没有简介哦还没有简介哦还没有简介哦还没有简介哦还没有简介哦"
        }
    },

    mounted() {
        var _this = this;
        console.log(_this.name);
          
    },
    methods: {
        toChange(){
            wx.navigateTo({url: '../userInfoChange/main'})
        },
    },
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

.userInfo-data{
    width: 600rpx;
    height: 700rpx;
    line-height: 60rpx;
    margin-top: 30rpx;
    font-size: 35rpx;
    /* border: 2px solid rgb(180, 109, 109); */
}

.userInfo-intro{
    width: 500rpx;
    margin-left: 50rpx;
    line-height: 40rpx;
    font-size: 30rpx;
    margin-top: 5rpx;
}

.userInfo-change{
    flex-direction:column; 
    height: 90rpx;
    width: 300rpx;
    margin-top: 30rpx;
    font-size: 50rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    display: flex;
    justify-content:center;
    align-items: center;
}

</style>