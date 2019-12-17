//配置项

/* const loginUrl = 'http://140.143.155.46:80/wechat_login'
const identity = 'http://140.143.155.46:80/wechat_identity' */

const loginUrl = 'https://2019-a17.iterator-traits.com/wechat_login'
const identity = 'https://2019-a17.iterator-traits.com/wechat_identity'
const userInfoChange = 'https://2019-a17.iterator-traits.com/edit_user'
const userInfo= 'https://2019-a17.iterator-traits.com/send_user_info'
const messageList = 'https://2019-a17.iterator-traits.com/get_message_list'
const messageDetail = 'https://2019-a17.iterator-traits.com/get_detail_message'
const activityInfo= 'https://2019-a17.iterator-traits.com/get_activity'



const config ={
    loginUrl,
    identity,
    userInfoChange,
    userInfo,
    messageList,
    messageDetail,
    activityInfo
}

export default config