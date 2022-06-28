<template>
  <div>
    <button @click="getWeather">[날씨정보받기]</button>
    <button @click="getDate">[시간출력]</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_KEY = '91356a12e2cf5bb611637fad75efd1cf'
const Curr_Weather_URL = 'https://api.openweathermap.org/data/2.5/weather'
const Back_URL = 'http://127.0.0.1:8000/weathers/'
const getTime = [0, 3, 6, 9, 12, 15, 18, 21]


export default {
  name: 'App',
  components: {

  },
  data: function () {
    return {
      wi: Object,
      date: Object,
    }
  },
  watch: {
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

    date: function (newVal, oldVal) {
      console.log('시각정보??!?!?', oldVal)
      if (getTime.includes(newVal.hours) && newVal.minutes === 0 && newVal.seconds === 0) {
        this.getWeather()
      }
    }
  },

  methods: {
    getWeather() {
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

  created() {
    setInterval(() => {
      this.getDate()
    }, 1000)
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
