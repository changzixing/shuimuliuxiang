<template>
    <div class = "box">
        <div class="left">
            <div class="left_1">{{user.userRank}}</div>
            <div class="left_2">{{user.userName}}</div>
        </div>
        <div class="right">{{user.userScore}}</div>
    </div>
</template>

<script>
export default {
    props: ["user"]
}
</script>

<style>
.box{
    position: relative;     
    display:flex;  
    flex-direction:row;  
    align-items: center;
    /* border: 2rpx solid rgb(180, 109, 109); */
    height: 100rpx;
    margin: 10rpx;
    border: 2px solid #fff;  
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
    justify-content: space-between;
    width: 700rpx;
}

.left{
    display:flex;  
    flex-direction:row;
    align-items: center;
    justify-content: center;
}

.left_1{
    width: 80rpx;
    margin: 30rpx;
    align-items: center;
    justify-content: center;
}

.left_2{
    width: 100rpx;
    margin: 20rpx;
    align-items: center;
    justify-content: center;
}

.right{
    width: 100rpx;
    margin: 30rpx;
    align-items: center;
    justify-content: center;
}
</style>