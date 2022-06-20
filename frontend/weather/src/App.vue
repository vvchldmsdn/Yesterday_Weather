<template>
  <div>
    <img alt="Vue logo" src="./assets/logo.png">
    <button @click="onClick">날씨받기</button>
    <current-weather :weather='data'></current-weather>
  </div>
</template>

<script>
import axios from 'axios'
import CurrentWeather from '@/components/CurrentWeather'

const API_KEY = '91356a12e2cf5bb611637fad75efd1cf'
const Curr_Weather_URL = 'https://api.openweathermap.org/data/2.5/weather'
const Back_URL = 'http://127.0.0.1:8000/weathers/'

export default {
  name: 'App',
  components: {
    CurrentWeather,
  },
  data: function () {
    return {
      wi: Object,
      data: Object,
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
        this.wi = res.data
        this.data = {
          temp: this.wi.main.temp,
          feels_like: this.wi.main.feels_like,
          humidity: this.wi.main.humidity,
          wind_speed: this.wi.wind.speed,
          wind_deg: this.wi.wind.deg,
          cloud: this.wi.clouds.all,
        }
      })
      .catch(err => {
        console.log(err)
      })
    },

    postWeather() {
      axios({
        method: 'post',
        url: Back_URL,
        data: this.data,
      })
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },

    onClick() {
      this.getWeather()
      this.postWeather()
    }

  }
}

</script>

<style>

</style>
