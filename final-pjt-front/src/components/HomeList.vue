<template>
  <div class="wrap-home-list">
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
