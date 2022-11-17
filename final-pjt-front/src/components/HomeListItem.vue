<template>
  <div>
    <h5>{{ movie.id }}</h5>
    <p>{{ movie.title }}</p>
    <span v-for="genre in genres" :key="genre.id">
      <span v-if="movie.genre_ids.includes(genre.id)">
        {{ genre.name }}
      </span>
    </span>
  </div>
</template>

<script>
export default {
  name: "HomeListItem",
  props: {
    movie: Object,
  },
  computed: {
    genres() {
      return this.$store.state.genres;
    },
  },
};
</script>

<style></style>
