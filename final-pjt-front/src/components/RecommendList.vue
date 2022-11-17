<template>
  <div>
    <h1>RecommendList</h1>
    <button @click="toggleClassic">
      <span v-if="!isClassic">고전 명작 on </span>
      <span v-if="isClassic">고전 명작 off </span>
    </button>
    <button @click="toggleIndependent">
      <span v-if="!isIndependent">독립 영화 on </span>
      <span v-if="isIndependent">독립 영화 off </span>
    </button>

    <hr />
    <RecommendListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      :isClassic="isClassic"
      :isIndependent="isIndependent"
    />
  </div>
</template>

<script>
import RecommendListItem from "./RecommendListItem.vue";

export default {
  name: "RecommendList",
  components: {
    RecommendListItem,
  },
  data() {
    return {
      isClassic: false,
      isIndependent: false,
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
  methods: {
    toggleClassic() {
      this.isClassic = !this.isClassic;
    },
    toggleIndependent() {
      this.isIndependent = !this.isIndependent;
    },
  },
};
</script>

<style></style>
