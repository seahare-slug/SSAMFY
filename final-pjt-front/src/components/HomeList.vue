<template>
  <div class="wrap-home-list">
    <HomeListItem v-for="movie in randomMovie" :key="movie.id" :movie="movie" />
  </div>
</template>

<script>
import HomeListItem from "./HomeListItem.vue";
import _ from "lodash";

export default {
  name: "HomeList",
  components: {
    HomeListItem,
  },
  data() {
    return{
      randomMovie: [],
    }
  },
  created() {
    this.randomMovie = _.sampleSize(this.movies, 200)
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    genres() {
      return this.$store.state.genres;
    },
  },
};
</script>

<style scoped>
.wrap-home-list {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-evenly;
}
</style>
