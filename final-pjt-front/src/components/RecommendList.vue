<template>
  <div>
    <div class="movie-filter">
      <div
        :class="{ 'common-btn': !isClassic, 'common-clicked-btn': isClassic }"
        @click="toggleClassic"
      >
        <span v-if="isClassic">고전 명작 on </span>
        <span v-if="!isClassic">고전 명작 off </span>
      </div>
      <div
        :class="{
          'common-btn': !isIndependent,
          'common-clicked-btn': isIndependent,
        }"
        @click="toggleIndependent"
      >
        <span v-if="isIndependent">독립 영화 on </span>
        <span v-if="!isIndependent">독립 영화 off </span>
      </div>
    </div>
    <div class="wrap-recommand-list">
      <RecommendListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        :isClassic="isClassic"
        :isIndependent="isIndependent"
      />
    </div>
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

<style scoped>
.wrap-recommand-list {
  margin: 0 auto;
  display: flex;
  flex-flow: row wrap;
}
.movie-filter {
  margin-bottom: 30px;
  display: flex;
  flex-direction: row-reverse;
}
</style>
