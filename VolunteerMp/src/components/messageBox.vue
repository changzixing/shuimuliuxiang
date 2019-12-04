<template>
    <div class = "box">
        <img src="../../static/images/tabbar_personalpage.png">
        <div class="message">
            <div class="messageSource">
                {{message.source}}
            </div>
            <div class="messageInfo">
                {{message.info}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ["message"]
}
</script>

<style>
.box{
    position: relative;     
    display:flex;  
    flex-direction:row;  
    /*align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109); */
    height: 120rpx;
    margin: 10rpx;
    border: 2px solid #fff;  
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
}

.box img{
    overflow:hidden;  
    display: block;  
    width: 100rpx;  
    height: 100rpx;  
    margin: 10rpx 30rpx;    
    border-radius: 50%;   
}

.message{
    display:flex;  
    flex-direction:column;  
   /*  align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109);  */
    height: 120rpx;
    width: 450rpx;
}

.messageSource{
    font-size:50rpx;
    height: 60rpx;
    /* border: 2rpx solid rgb(180, 109, 109); */
    margin: 5rpx;
    display: flex;             
    align-items: center;
}

.messageInfo{
    font-size:30rpx;
    height: 40rpx;
    /* border: 2rpx solid rgb(180, 109, 109); */
    margin: 5rpx;
    display: flex;             
    align-items: center; 
}

</style>