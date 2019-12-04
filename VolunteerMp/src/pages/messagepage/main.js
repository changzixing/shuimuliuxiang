import Vue from 'vue'
import Messagepage from './messagepage'
import messagebox from "@/components/messageBox"

Vue.use(messagebox);

const app = new Vue(Messagepage)
app.$mount()