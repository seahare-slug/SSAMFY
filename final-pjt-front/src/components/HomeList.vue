<template>
  <div class="wrap-home-list">
    <HomeListItem v-for="movie in randomMovie" :key="movie.id" :movie="movie" />
    <button @click="getNowplayMovies">현재 상영 중인 영화 보기</button>
    <div v-for="nmovie in nowmovies"
        :key="nmovie.id"
      >
      {{nmovie.title}}
      <img :src="`https://image.tmdb.org/t/p/w500/${nmovie.poster_path}`" alt="">
      <div>
      <router-link
        class="common-btn"
        :to="{ name: 'DetailView', params: { id: nmovie.id } }"
        >DETAIL</router-link
      >
    </div>
    </div>
  </div>
</template>

<script>
import HomeListItem from "./HomeListItem.vue";
import _ from "lodash";
import axios from "axios";

export default {
  name: "HomeList",
  components: {
    HomeListItem,
  },
  data() {
    return{
      randomMovie: [],
      nowmovies : []
    }
  },
  created() {
    this.randomMovie = _.sampleSize(this.movies, 30)
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    genres() {
      return this.$store.state.genres;
    },
  },
  methods:{
    getNowplayMovies(){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/now_playing?api_key=616c881ba896937b008706b9a5e911d0&language=ko-KR&page=1`
      })
      .then((res) =>{
        this.nowmovies = res.data.results
      })
    }
  }
};
</script>

<style scoped>
.wrap-home-list {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-evenly;
}
</style>
