<template>
  <div>
    <span
      v-if="
        isClassic === true &&
        movie.release_date.slice(0, 4) < 2022 &&
        movie.vote_average > 7.5 &&
        isIndependent === true &&
        50 < movie.vote_count &&
        movie.vote_count < 200 &&
        movie.vote_average > 7
      "
    >
      <h5>{{ movie.title }}</h5>
      <p>{{ movie.vote_average }}</p>
      <p>{{ movie.release_date }}</p>
      <p>{{ movie.original_title }}</p>
    </span>
    <span
      v-if="
        isClassic === false &&
        isIndependent === true &&
        50 < movie.vote_count &&
        movie.vote_count < 200 &&
        movie.vote_average > 7
      "
    >
      <h5>{{ movie.title }}</h5>
      <p>{{ movie.vote_average }}</p>
      <p>{{ movie.release_date }}</p>
      <p>{{ movie.original_title }}</p>
    </span>
    <span
      v-if="
        isClassic === true &&
        movie.release_date.slice(0, 4) < 2022 &&
        movie.vote_average > 7.5 &&
        isIndependent === false
      "
    >
      <h5>{{ movie.title }}</h5>
      <p>{{ movie.vote_average }}</p>
      <p>{{ movie.release_date }}</p>
      <p>{{ movie.original_title }}</p>
    </span>
    <span v-if="isClassic === false && isIndependent === false">
      <h5>{{ movie.title }}</h5>
      <p>{{ movie.vote_average }}</p>
      <p>{{ movie.release_date }}</p>
      <p>{{ movie.original_title }}</p>
    </span>
  </div>
</template>

<script>
export default {
  name: "RecommendListItem",
  props: {
    movie: Object,
    isClassic: Boolean,
    isIndependent: Boolean,
  },
  computed: {
    genres() {
      return this.$store.state.genres;
    },
  },
};
</script>

<style></style>
