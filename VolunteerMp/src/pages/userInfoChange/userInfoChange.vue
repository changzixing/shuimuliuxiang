<template>
    <div class="userInfo">
        <div class="userInfo-data">
            <div>姓名：{{name}}</div>
            <div>学号：{{studentId}}</div>
            <div>院系：{{school}}</div>
            <div class="userInfo-change">
                <div>性别：</div>
                <input type="text" v-model="sex">
            </div>
            <div class="userInfo-change">
                <div>志愿北京编号：</div>
                <input type="text" v-model="volunteerId">
            </div>
            <div class="userInfo-change">
                <div>联系电话：</div>
                <input type="text" v-model="phoneNumber">
            </div>
            <div class="userInfo-change">
                <div>联系邮箱：</div>
                <input type="text" v-model="email">
            </div>
            <div class="userInfo-change">
                <div>公益兴趣：</div>
                <input type="text" v-model="interest">
            </div>
            <div class="userInfo-change">简介：</div>
            <div class="userInfo-change-intro">
                <input type="text" v-model="introduction">
            </div>
        </div>
        
        <div class="userInfo-changeDone">
            提交修改
        </div>
    </div>
</template>

<script>
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

.userInfo-data{
    width: 600rpx;
    line-height: 60rpx;
    margin-top: 30rpx;
    font-size: 35rpx;
    /* border: 2px solid rgb(180, 109, 109); */
}

.userInfo-change{
    display: flex;
    flex-direction: row;
    width: 600rpx;
    align-items: center;
    
    /* border: 2px solid rgb(180, 109, 109); */
}

.userInfo-change input{
    border: 2px solid rgb(180, 156, 174);
}

.userInfo-change-intro{
    width: 500rpx;
    height: 300rpx;
    margin-left: 50rpx;
    line-height: 40rpx;
    font-size: 30rpx;
    margin-top: 5rpx;
    border: 2px solid rgb(180, 156, 174);
}




.userInfo-changeDone{
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