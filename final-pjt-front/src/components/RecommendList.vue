<template>
  <div>
    <h1>RecommendList</h1>
    <hr>
    <RecommendListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import RecommendListItem from './RecommendListItem.vue';

export default {
    name: 'RecommendList',
    components:{
        RecommendListItem
    },
    computed: {
        movies() {
            return  this.$store.state.movies
        }
    }
}
</script>

<style>

</style>