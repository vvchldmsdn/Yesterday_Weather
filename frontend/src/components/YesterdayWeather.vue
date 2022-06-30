<template>
  <div>
    <h1
      v-for="showData in showDatas"
      :key="showData.id"
    >{{ showData.temp }}, {{ showData.id }}</h1>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: "YesterdayWeather",
  props: {
    yesterdayDatas: Array,
  },
  data: function () {
    return {
      realData: Array,
    }
  },
  computed: {
    showDatas: function () {
      return this.yesterdayDatas
    }
  }
}
</script>

<style>

</style>