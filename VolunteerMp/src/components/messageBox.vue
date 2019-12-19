<template>
    <div class = "box">
        <img src="../../static/images/message.png">
        <div class="message">
            <div class="messageSource">
                {{message.name}}
            </div>
            <div class="messageInfo">
                {{message.content}}
            </div>
        </div>
        <div class = "messageMore">
            <div class = "messageTime">
                {{makeTime}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ["message"],
    computed: {
        makeTime(){
            let time = this.message.time;
            let timestamp = Date.parse(new Date());
            let date = new Date(timestamp);
            let year_n = date.getFullYear();
            let month_n = date.getMonth() + 1;
            let date_n = date.getDate();

            let str = time.split(" ");     
            let str_date_list = str[0].split("-")
            let str_time_list = str[1].split(":")

            let year = Number(str_date_list[0])
            let month = Number(str_date_list[1])
            let date_c = Number(str_date_list[2])

            if(year_n === year)
            {
                if(month_n === month && date_c === date_n)
                {
                    return str_time_list[0] + ":" + str_time_list[1]
                }
                else
                {
                    return String(month) + "-" +String(date_c)
                }
            }
            else
            {
                return String(year) + "-" +String(month)
            }

        },
    },
    
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
    margin: 20rpx;
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

.message{
    display:flex;  
    flex-direction:column;  
   /*  align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109);  */
    height: 100rpx;
    width: 450rpx;
}

.messageSource{
    font-size:40rpx;
    height: 45rpx;
    /* border: 2rpx solid rgb(180, 109, 109); */
    margin: 5rpx;
    display: flex;             
    align-items: center;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.messageInfo{
    font-size:30rpx;
    height: 40rpx;
    /* border: 2rpx solid rgb(180, 109, 109); */
    margin: 5rpx;
    display: flex;             
    align-items: center;
    color: rgb(116, 106, 106);
}

.messageMore{
    display:flex;  
    flex-direction:column;  
   /*  align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109);  */
    height: 100rpx;
}

.messageTime{
    margin: 5rpx;
    height: 30rpx;
    font-size:25rpx;
    display: flex;             
    align-items: center; 
}

</style>