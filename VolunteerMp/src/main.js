import Vue from 'vue'
import App from './App'
import Global from './global.js'

Vue.config.productionTip = false

const app = new Vue({
    App,
    mpType: 'app'
})
app.$mount()
Vue.prototype.GLOBAL = Global
export default{

}

