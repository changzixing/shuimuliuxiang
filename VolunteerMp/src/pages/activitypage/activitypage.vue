<template>
    <view class="activityPage">
            <view class="search-1">
                <input class="textBar" name="text">
                <view class="searchButton">搜索</view>
            </view>
            <view class="search-2">
                <view v-for="searchFlag in searchFlags" :key="searchFlag.name" :class="searchFlag.picked ? 'searchFlag1' : 'searchFlag2'" @click="searchFlagChange(searchFlag)">{{searchFlag.value}}</view>
            </view>
            <view class="activity-1">
                <view v-for="activityType in activityTypes" :key="activityType.code" :class="activityType.picked ? 'activityType1' : 'activityType2'" @click="activityTypeChange(activityType)">{{activityType.value}}</view>
            </view>
            <view class="activity-2">
                <view v-for="sortFlag in sortFlags" :key="sortFlag.name" :class="sortFlag.picked ? 'sortFlag1' : 'sortFlag2'" @click="sortFlagChange(sortFlag)">{{sortFlag.value}}</view>
            </view>
            <view class="activity-3">
                <activitybox v-for="activity in activities" :key="activity.id" :activity="activity"></activitybox>
            </view>
            <view class="activity-4">
                <view @click="lastPage()">上一页</view>
                <view>{{pageNum}} / {{pageAll}}</view>
                <view @click="nextPage()">下一页</view>
            </view>
        </view>
</template>

<script>
import qcloud from 'wafer2-client-sdk'
import config from '@/config.js'
import activitybox from "@/components/activityBox"
export default {
    components:{
        activitybox
    },

    created() {
        console.log('activitypage ready')
    },

    onShow() {
        var _this = this;
        wx.request({
            url:config.activityInfo,
            dataType: "json",
            data: {
                openID:_this.GLOBAL.openid,
                sortFlag:_this.sortFlag,
                pageNum:_this.pageNum,
                activityType:_this.activityType,
            },
            method: 'POST',
            header: { 'content-type': 'application/x-www-form-urlencoded'},
            success: function (res) {
                if (res.statusCode == 200) {
                    if(res.data.error){

                    }
                    else{
                        _this.activities = res.data.content;
                        _this.pageAll = res.data.page;
                    }
                }
                else {
                    console.log(res.errMsg);
                }
                console.log(res)
            },
        })
        
    },

    mounted() {
        
    },

    data() {
        return {
            searchKeyWord:"",
            searchFlag:"name",
            searchFlags:[
                { name: 'name', value: '活动名称', picked: true},
                { name: 'owner', value: '活动发起方', picked: false},
            ],
            activityType:[
                '0','1','2','3','4','5'
            ],
            activityTypes:[
                { code: '0', value: '文化教育', picked: true},
                { code: '1', value: '赛会服务', picked: true},
                { code: '2', value: '社区服务', picked: true},
                { code: '3', value: '医疗卫生', picked: true},
                { code: '4', value: '健康残障', picked: true},
                { code: '5', value: '其他类型', picked: true},
            ],
            sortFlags:[
                { name: 'time', value: '时间', picked: true},
                { name: 'hot', value: '热度', picked: false},
                { name: 'notFull', value: '未招满', picked: false},
            ],
            sortFlag: "time",
            activities:[

            ],
            pageNum: 1,
            pageAll: 1,
        }
    },

    methods: {
        searchFlagChange(searchFlag){
            var _this = this;
            for(var i in _this.searchFlags)
            {
                _this.searchFlags[i].picked = false;
            }
            searchFlag.picked = true;
            _this.searchFlag = searchFlag.name;
        },
        activityTypeChange(activityType){
            var _this = this;
            var activityTypes = [];
            activityType.picked = !activityType.picked;
            for(var i in _this.activityTypes)
            {
                if(_this.activityTypes[i].picked == true)
                {
                    activityTypes.push(_this.activityTypes[i].code);
                }
            }
            _this.activityType = activityTypes;
            _this.pageNum = 1;
            _this.$mp.page.onShow();
        },
        sortFlagChange(sortFlag){
            var _this = this;
            for(var i in _this.sortFlags)
            {
                _this.sortFlags[i].picked = false;
            }
            sortFlag.picked = true;
            _this.sortFlag = sortFlag.name;
            _this.pageNum = 1;
            _this.$mp.page.onShow();
        },
        lastPage(){
            var _this = this;
            if(_this.pageNum > 1)
            {
                _this.pageNum -= 1;
                _this.$mp.page.onShow();
            }
        },
        nextPage(){
            var _this = this;
            if(_this.pageNum < _this.pageAll)
            {
                _this.pageNum += 1;
                _this.$mp.page.onShow();
            }
        },
        /*
        search(){
            var _this = this;
            wx.request({
            })
        },
        toActivityInfo(){
            wx.navigateTo({url: '../activityInfo/main'})
        },
        */
    },

    
}
</script>

<style>
.activityPage {
    width: 700rpx;
    height: 1050rpx;
    margin: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    border: 2rpx solid #000;
}

.search-1 {
    width: 600rpx;
	height: 80rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.search-2 {
    width: 600rpx;
	height: 70rpx;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.textBar {
    width: 450rpx;
    height: 66rpx;
    font-size: 40rpx;
    color: #000;
    border: 2rpx solid rgb(122, 114, 189);
}

.searchButton {
    width: 150rpx;
    height: 70rpx;
    font-size: 40rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    border-radius: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.activity-1 {
    width: 600rpx;
    height: 120rpx;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
    align-content: space-around;
}

.activity-2 {
    width: 600rpx;
    height: 70rpx;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.activity-3 {
    width: 600rpx;
    height: 640rpx;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.activity-4 {
    width: 600rpx;
    height: 60rpx;
    font-size: 35rpx;
    color: rgb(122, 114, 189);
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.searchFlag1 {
    width: 270rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.searchFlag2 {
    width: 270rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.activityType1 {
    width: 180rpx;
    height: 50rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    border: 2rpx solid rgb(122, 114, 189);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.activityType2 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: rgb(122, 114, 189);
    border: 2rpx solid rgb(122, 114, 189);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.sortFlag1 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.sortFlag2 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
</style>