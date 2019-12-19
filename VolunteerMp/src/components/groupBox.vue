<template>
    <div class = "box">
        <img :src= "'https://2019-a17.iterator-traits.com/media/'+ group.groupHead">
        <div class="group">
            <div class="groupName">
                {{group.groupName}}
            </div>
        </div>
        <div class = "groupMore">

        </div>
    </div>
</template>

<script>
export default {
    props: ["group"],
}
</script>

<style>
.box{
    position: relative;     
    display:flex;  
    flex-direction:row;  
    /*align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109); */
    height: 100rpx;
    margin: 10rpx;
    border: 2px solid #fff;  
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
}

.box img{
    overflow:hidden;  
    display: block;  
    width: 80rpx;  
    height: 80rpx;  
    margin: 10rpx 30rpx;    
    border-radius: 50%;   
}

.group{
    display:flex;  
    flex-direction:column;  
   /*  align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109);  */
    height: 100rpx;
    width: 450rpx;
}

.groupName{
    font-size:40rpx;
    height: 90rpx;
    /* border: 2rpx solid rgb(180, 109, 109); */
    margin: 5rpx;
    display: flex;             
    align-items: center;
}

.groupMore{
    display:flex;  
    flex-direction:column;  
   /*  align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109);  */
    height: 100rpx;
}


</style>