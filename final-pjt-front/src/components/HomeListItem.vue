<template>
  <div>
    <h2>{{ movie.title }}</h2>
    <p>{{ movie.vote_average }}</p>
    <span v-for="genre in genres" :key="genre.id">
      <span v-if="movie.genre_ids.includes(genre.id)">
        {{ genre.name }}
      </span>
    </span>
    <router-link :to="{ name: 'DetailView', params: { id: movie.id } }"
      >[DETAIL]</router-link
    >
    <hr />
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
  // methods: {
  //   moveToDetail() {
  //     return this.$router.push({ name: `DetailView/${this.movie.id}` });
  //   },
  // },
};
</script>

<style></style>
