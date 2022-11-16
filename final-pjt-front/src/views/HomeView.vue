<template>
  <div>
    <h1>Home</h1>
    <hr>
    <HomeList/>
  </div>
</template>

<script>
import HomeList from '../components/HomeList.vue'

export default {
    name: 'HomeView',
    components: {
        HomeList,
    },
    created(){
      this.getMovies()
    },
    methods:{
      getMovies(){
        this.$store.dispatch('getMovies')
      }
    }
}
</script>

<style>

</style>