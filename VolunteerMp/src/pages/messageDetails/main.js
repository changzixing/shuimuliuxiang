import Vue from 'vue'
import MessageDetails from './messageDetails'
import messagebox from "@/components/messageBox"

Vue.use(messagebox);

const app = new Vue(MessageDetails)
app.$mount()