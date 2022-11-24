<template>
  <div>
    <div class="common-btn reload-btn" @click="getNowplayMovies">
      현재 상영 중인 영화 보기
    </div>
    <div id="wrapSimilar" class="wrap-similar toggle-similar">
      <div class="similar-movie" v-for="nmovie in nowmovies" :key="nmovie.id">
        <h3 class="hide-title">{{ nmovie.title }}</h3>
        <img
          class=""
          :src="`https://image.tmdb.org/t/p/w500/${nmovie.poster_path}`"
          alt="nmovie_poster"
        />
        <div>
          <router-link
            class="common-btn"
            :to="{ name: 'DetailView', params: { id: nmovie.id } }"
            >DETAIL</router-link
          >
        </div>
      </div>
    </div>
    <div class="common-btn reload-btn" @click="HomeReload">
      새로운 영화 목록 보기
    </div>
    <form class="wrap-search-form" action="">
      <input type="text" v-model="find" />
      <button @click.prevent="findMovie">검색</button>
    </form>
    <div class="wrap-home-list">
      <HomeListItem
        v-for="movie in randomMovie"
        :key="movie.id"
        :movie="movie"
      />
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
    return {
      randomMovie: [],
      nowmovies: [],
      find: null,
    };
  },
  created() {
    this.randomMovie = this.movies.slice(21, 53);
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
    getNowplayMovies() {
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/now_playing?api_key=616c881ba896937b008706b9a5e911d0&language=ko-KR&page=1`,
      }).then((res) => {
        this.nowmovies = res.data.results;
        this.viewSimilarMovies()
      });
    },
    HomeReload() {
      this.randomMovie = _.sampleSize(this.movies, 32);
    },
    findMovie() {
      this.randomMovie = this.movies.filter((movie) =>
        movie.title.includes(this.find)
      );
    },
    viewSimilarMovies() {
      const wrapSimilar = document.querySelector("#wrapSimilar");
      wrapSimilar.classList.toggle("toggle-similar");
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
.reload-btn {
  width: 80%;
  margin: 20px auto;
}
.wrap-search-form {
  text-align: right;
  margin: 30px 0 20px 0;
}
.wrap-search-form button {
  margin: 5px;
}
.wrap-similar {
  position: relative;
  z-index: 1000;
  background-color: rgba(216, 112, 147, 0.3);
  display: flex;
  flex-wrap: nowrap;
  overflow-x: scroll;
  overflow-y: hidden;
}
.toggle-similar {
  display: none;
}
.hide-title {
  display: none;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.similar-movie {
  cursor: pointer;
  position: relative;
  margin: 2%;
  width: 200px;
  flex: 0 0 auto;
}
.similar-movie img {
  width: 10vw;
}
</style>
