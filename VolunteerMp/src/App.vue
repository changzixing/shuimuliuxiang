
<script>
import qcloud from 'wafer2-client-sdk'
import config from './config'
export default{
    created() {
        console.log('start')
    },
    onShow(){
        var _this = this;
        if(_this.$root.$mp.appOptions.referrerInfo.extraData){
            _this.token = _this.$root.$mp.appOptions.referrerInfo.extraData.token;
            console.log(_this.token);
        }
        console.log(_this.$root.$mp);
        
    },
}
</script>

<style>
    
</style>