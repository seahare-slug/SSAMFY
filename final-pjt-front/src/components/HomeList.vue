<template>
  <div>
    <h1>HomeList</h1>
    <hr />
    <HomeListItem v-for="movie in movies" :key="movie.id" :movie="movie" />
  </div>
</template>

<script>
import HomeListItem from "./HomeListItem.vue";

export default {
  name: "HomeList",
  components: {
    HomeListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    genres() {
      return this.$store.state.genres
    }
  },
  created(){
    console.log(this.genres)
  }
};
</script>

<style></style>
