<template>
  <div>
    <div>
      <h1>Detail</h1>
      <p>글 번호 : {{ detailViewData.movie?.id }}</p>
      <p>제목 : {{ detailViewData.movie?.title }}</p>
      <p>줄거리 : {{ detailViewData.movie?.overview }}</p>
      <span v-for="genre in genres" :key="genre.id">
        <span v-if="detailViewData.movie?.genre_ids.includes(genre.id)">
          {{ genre.name }}
        </span>
        <!-- {{detailViewData.movie.genre_ids}} -->
      </span>
    </div>
    <div>
      <form>
        <input
          v-model="detailViewData.content"
          type="text"
          name="content"
          id="content"
        />
        <button @click.prevent="submitComment">댓글 작성</button>
      </form>
      <CommentList/>
      <button @click="getsimilarMovies">비슷한 영화 보러 가기</button>
      <div v-for="smovie in newmovies"
        :key="smovie.id"
      >
      {{smovie.title}}
      <img :src="`https://image.tmdb.org/t/p/w500/${smovie.poster_path}`" alt="">
      <!-- <router-link
        class="common-btn"
        :to="{ name: 'DetailView', params: { id: smovie.id } }"
        >DETAIL</router-link
      > -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import CommentList from "@/components/CommentList.vue";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "DetailView",
  components: {
    CommentList,
  },
  computed: {
      genres() {
        return this.$store.state.genres;
      },
  },
  data() {
    return {
      detailViewData: {
        movie: null,
        content: null,
        username: localStorage.getItem("userName"),
      },
      commnents: [],
      newmovies:[],
    };
  },
  created() {
    this.getArticleDetail();
    this.getComments();
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}`,
      })
        .then((res) => {
          this.detailViewData.movie = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    submitComment() {
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movies/${this.detailViewData.movie.id}/comment/create/`,
        data: this.detailViewData,
      })
        .then(() => {
          console.log("======Vue에서 데이터 보냄======");
          this.detailViewData.content = null;
        })
        .then(() => {
          this.getComments();
          // this.$router.push({ name: "DetailView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getComments() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/comment/`,
      })
        .then((res) => {
          this.comments = res.data;
          this.$store.dispatch("getComments", this.comments);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getsimilarMovies(){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.detailViewData.movie.id}/similar?api_key=616c881ba896937b008706b9a5e911d0&language=ko-KR&page=1`
      })
      .then((res) =>{
        this.newmovies = res.data.results
      })
    }
  },
};
</script>
