<template>
    <div>
        <div class="time">{{makeTime}}</div>
        <div class = "box">
            <img src="../../static/images/tabbar_personalpage.png">
            <div class="message">
                <div class="messageInfo">
                    {{message.content}}
                </div>
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
            let month_n = date.getMonth();
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
                    return String(month) + "-" +String(date_c) + ' ' + str_time_list[0] + ":" + str_time_list[1]
                }
            }
            else
            {
                return String(year) + "-" +String(month) + "-" +String(date_c)
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
    /* height: 120rpx; */
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

.message{
    display:flex;  
    flex-direction:column;  
   /*  align-items: center;*/
    /* border: 2rpx solid rgb(180, 109, 109);  */
    height: 120rpx;
    width: 450rpx;
}

.messageInfo{
    font-size:30rpx;
    /* border: 2rpx solid rgb(180, 109, 109); */
    margin: 10rpx;
    display: flex;             
    align-items: center; 
}

.time{
    position: relative;      
    display:flex;  
    flex-direction:column;  
    align-items: center;
    margin: 20rpx;
    font-size: 20rpx;  
}
</style>