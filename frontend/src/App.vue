<template>
  <div>
    <button @click="getWeather">[날씨정보받기]</button>
    <button @click="getDate">[시간출력]</button>
    <button @click="getYesterdayWeather">[어제날씨 수동으로]</button>
    <yesterday-weather :yesterday-datas="yesterdayDatas"></yesterday-weather>
    <!-- <YesterdayWeather v-bind:midnight="isMidnight"/> -->
  </div>
</template>

<script>
// 여기서는 딱 데이터 받는 것만 하자
// 데이터 다 props로 넘겨서 거기서 해결

import axios from 'axios'
import yesterdayWeather from './components/YesterdayWeather.vue'

const API_KEY = '91356a12e2cf5bb611637fad75efd1cf'
const Curr_Weather_URL = 'https://api.openweathermap.org/data/2.5/weather'
const Back_URL = 'http://127.0.0.1:8000/weathers/'


export default {
  name: 'App',
  components: {
    yesterdayWeather
  },
  data: function () {
    return {
      wi: Object,
      date: Object,
      isMidnight: 0,
      yesterdayDatas: Array,
    }
  },
  watch: {
    // 4. wi가 업데이트 되면 백엔드에 저장 시킴
    wi: function (newVal, oldVal) {
      console.log('올드발', oldVal)

      const postData = {
        temp: newVal.main.temp,
        feels_like: newVal.main.feels_like,
        humidity: newVal.main.humidity,
        wind_speed: newVal.wind.speed,
        wind_deg: newVal.wind.deg,
        cloud: newVal.clouds.all,
      }
      axios({
        method: 'post',
        url: Back_URL,
        data: postData,
      })
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },

    // 2. 정각이 되면 getWeather를 실행시켜 날씨 정보를 받아옴
    date: function (newVal, oldVal) {
      console.log('시각정보??!?!?', oldVal)
      if (newVal.minutes === 0 && newVal.seconds === 0) {
        this.getWeather()
        this.getYesterdayWeather()
      }
    }
  },

  methods: {
    getYesterdayWeather() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/weathers/'
      })
      .then(res => {
        this.yesterdayDatas = res.data
        console.log(this.yesterdayDatas)
      })
    },
    
    // 3. 날씨 정보를 받아오면서 wi를 업데이트 시킴
    getWeather() {
      console.log('정각이다 받아오자!')
      const params = {
        appid: API_KEY,
        lat: 37,
        lon: 127,
      }
      axios({
        method: 'get',
        url: Curr_Weather_URL,
        params: params,
      })
      .then(res => {
        console.log('날씨 정보', res.data)
        this.wi = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
 
    getDate() {
      const nowDate = new Date()
      const hours = nowDate.getHours()
      const minutes = nowDate.getMinutes()
      const seconds = nowDate.getSeconds()
      console.log('시각', nowDate)
      this.date = {
        hours: hours,
        minutes: minutes,
        seconds: seconds
      }
    }
  },

  // 1. 매 초 시간 정보를 받아옴
  created() {
    setInterval(() => {
      this.getDate()
    }, 1000),
    this.getYesterdayWeather()
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
