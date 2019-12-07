<template>
    <div>
        <Messagebox v-for="message in messages" :key="message.id" :message="message"></Messagebox>
    </div>
</template>

<script>
import Messagebox from "@/components/messageBox"
export default {
    created() {
        console.log('messagepage ready')
    },
    components:{
        Messagebox
    },
    data(){
        return{
            messages:[
                {source:"1",info:"message1"},
                {source:"2",info:"message2"}
            ],
        }
    },
    methods: {
        toMoreMessage(){
            
        }
    },
}
</script>

<style>
.moreMessage{
    display: flex;  
    flex-direction:row;  
    height: 70rpx;
    font-size: 40rpx;  
    /* border: 2px solid rgb(202, 77, 77); */
    justify-content:space-between;
    align-items: center;
}
</style>