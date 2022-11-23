<template>
  <div>
    {{ likeList }}
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
import axios from "axios";
export default {
  name: "RecommendList",
  components: {
    RecommendListItem,
  },
  data() {
    return {
      username : localStorage.getItem('userName'),
      isClassic: false,
      isIndependent: false,
      movie_genres : {   
      '액션' : 5,
      '모험' : 5,
      '애니메이션' : 5,
      '코미디' : 5,
      '범죄' : 5,
      '다큐멘터리' : 5,
      '드라마' : 5,
      '가족' : 5,
      '판타지' : 5,
      '역사' : 5,
      '공포' : 5,
      '음악' : 5,
      '미스터리' : 5,
      '로맨스' : 5,
      'SF' : 5,
      'TV 영화' : 5,
      '스릴러' : 5,
      '전쟁' : 5,
      '서부' : 5,
      },
    likeList: [],
    };
  },
  created() {
    this.bringLike()
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    genres() {
      return this.$store.state.genres;
    },
  },
  methods: {
    toggleClassic() {
      this.isClassic = !this.isClassic;
    },
    toggleIndependent() {
      this.isIndependent = !this.isIndependent;
    },
    bringLike() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/liked/${this.username}/`,
      })
        .then((res) => {
          this.likeList = res.data.liked_movie
          console.log(this.movie_genres)
        
        })
        .catch((err) => {
          console.log(err)
        })
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
