<template>
  <div>
    <p>{{ weather }}</p>
  </div>
</template>

<script>

export default {
  name: 'CurrentWeather',
  props: {
    weather: Object,
  }
}
</script>

<style>

</style>
