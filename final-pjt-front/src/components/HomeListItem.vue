<template>
  <div class="wrap-home-item">
    <h4>{{ movie.title }}</h4>
    <img
      class="poster-img"
      :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
      alt="movie_poster"
    />
    <!-- DetailView로 이동 -->
    <!-- <span v-for="genre in genres" :key="genre.id">
      <span v-if="movie.genre_ids.includes(genre.id)">
        {{ genre.name }}
      </span>
    </span> -->
    <div>
      <router-link :to="{ name: 'DetailView', params: { id: movie.id } }"
        >[DETAIL]</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeListItem",
  props: {
    movie: Object,
  },
  computed: {
    // genres() {
    //   return this.$store.state.genres;
    // },
  },
};
</script>

<style scoped>
.wrap-home-item {
  border: black 3px solid;
  border-radius: 5px;
  width: 20%;
  height: 50vh;
  margin: 5px;
}
.poster-img {
  height: 70%;
}
</style>
