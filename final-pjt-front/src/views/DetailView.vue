<template>
  <div>
    <h1>Detail</h1>
    <div class="wrap-detail">
      <img
        :src="`https://image.tmdb.org/t/p/w500/${detailViewData.movie?.poster_path}`"
        alt="movie_poster"
      />
      <div class="wrap-detail-para">
        <div class="title">{{ detailViewData.movie?.title }}</div>
        <span v-for="genre in genres" :key="genre.id">
          <span
            class="genre"
            v-if="detailViewData.movie?.genre_ids.includes(genre.id)"
          >
            {{ genre.name }}
          </span>
        </span>
        <div class="overview">{{ detailViewData.movie?.overview }}</div>
        <div class="wrap-btn">
          <button class="common-btn" @click="viewSimilarMovies">비슷한 영화 보러 가기</button>
          <button class="common-btn" @click="viewCrews">출연진 보기</button>
        </div>
      </div>
    </div>
    <div id="wrapCrew" class="toggle-crews">
      <div class="wrap-crew">
        <div class="crew-info">
          <div class="hide-title">
            <h3>DIRECTOR</h3>
            <h4>[{{ director?.name }}]</h4>
          </div>
          <img
            :src="`https://image.tmdb.org/t/p/w500/${director?.profile_path}`"
            alt="profile"
          />
        </div>
        <div class="crew-info" v-for="cast in crews" :key="cast.id">
          <div class="hide-title">
            <h3>CAST</h3>
            <h4>[{{ cast.name }}]</h4>
          </div>
          <img
            :src="`https://image.tmdb.org/t/p/w500/${cast?.profile_path}`"
            alt="profile"
          />
        </div>
      </div>
    </div>
    <div>
      <button id="loadNewSimilarBtn" class="common-btn toggle-similar" @click="getSimilarMovies">새로운 영화 불러오기</button>
    </div>
    <div id="wrapSimilar" class="wrap-similar toggle-similar">
      <div class="similar-movie" v-for="smovie in newmovies" :key="smovie.id">
        <h3 class="hide-title">{{ smovie.title }}</h3>
        <img
          :src="`https://image.tmdb.org/t/p/w500/${smovie.poster_path}`"
          alt="smovie_poster"
        />
        <div>
          <router-link
            class="common-btn"
            :to="{ name: 'DetailView', params: { id: smovie.id } }"
            >DETAIL</router-link
          >
      </div>
    </div>
    </div>
    <div class="wrap-comment">
      <CommentList />
      <form>
        <input
          v-model="detailViewData.content"
          type="text"
          name="content"
          id="content"
        />
        <button @click.prevent="submitComment">댓글 작성</button>
      </form>
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
      newmovies: [],
      crews: [],
      director: null,
      similarPage: 1,
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
      if (!localStorage.getItem("userName")) {
        alert("로그인이 필요합니다.");
        this.$router.push({ name: "LoginView" });
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movies/${this.detailViewData.movie.id}/comment/create/`,
        data: this.detailViewData,
      })
        .then(() => {
          this.detailViewData.content = null;
        })
        .then(() => {
          this.getComments();
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
    getSimilarMovies() {
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/${this.detailViewData.movie.id}/similar?api_key=616c881ba896937b008706b9a5e911d0&language=ko-KR&page=${this.similarPage}`,
      }).then((res) => {
        this.newmovies = res.data.results;
        this.similarPage += 1;
      });
    },
    viewSimilarMovies() {
      const wrapSimilar = document.querySelector("#wrapSimilar");
      const loadNewSimilarBtn = document.querySelector("#loadNewSimilarBtn");
      if (this.newmovies.length === 0) {
        this.getSimilarMovies();
      }
      loadNewSimilarBtn.classList.toggle("toggle-similar")
      wrapSimilar.classList.toggle("toggle-similar");
    },
    getCrews() {
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/${this.detailViewData.movie.id}/credits?api_key=616c881ba896937b008706b9a5e911d0&language=ko-KR`,
      })
        .then((res) => {
          this.crews = res.data.cast.slice(0, 3);
          this.director = res.data.crew.filter(
            (crew) => crew.job === "Director"
          )[0];
        })
        .catch((err) => {
          console.log(err);
        });
    },
    viewCrews() {
      const wrapCrew = document.querySelector("#wrapCrew");
      if (this.crews.length === 0) {
        this.getCrews();
      }
      wrapCrew.classList.toggle("toggle-crews");
    },
  },
};
</script>

<style scoped>
h1 {
  margin: 5% auto;
}
.wrap-detail {
  margin-bottom: 2%;
  padding: 20px;
  display: flex;
  background-color: rgba(216, 112, 147, 0.3);
}
.wrap-detail img {
  width: 25vw;
}
.wrap-detail-para {
  padding: 0 10% 0 10%;
}
.wrap-btn button {
  margin: 10px
}
.title {
  font-size: 2.4rem;
  font-weight: bold;
  margin: 30px 0;
}
.genre {
  font-weight: bold;
  font-size: 1.7rem;
}
.overview {
  text-align: left;
  line-height: 30px;
  margin: 10% 0 5% 0;
  padding: 5%;
  background-color: rgba(245, 255, 255, 0.4);
  font-weight: bold;
}
.wrap-comment {
  padding: 5%;
  display: flex;
}
.wrap-comment form {
  margin: 5% auto;
}
.wrap-similar {
  background-color: rgba(216, 112, 147, 0.3);
  display: flex;
  flex-wrap: nowrap;
  overflow-x: scroll;
  overflow-y: hidden;
}
.hide-title {
  display: none;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.similar-movie, .crew-info {
  cursor: pointer;
  position: relative;
  margin: 2%;
  width: 200px;
  flex: 0 0 auto;
}
.wrap-crew {
  display: flex;
  justify-content: space-evenly;
  background-color: rgba(216, 112, 147, 0.3);
  margin-bottom: 50px;
}
.crew-info img {
  border-radius: 20%;
  border: rgb(216, 192, 200) 4px solid;
  width: 100%;
}
.similar-movie:hover > img {
  opacity: 0.2;
}

.crew-info:hover > img {
  opacity: 0.2;
}
.similar-movie:hover .hide-title {
  display: block;
}
.crew-info:hover .hide-title {
  display: block;
}
.similar-movie img {
  width: 100%;
}
.toggle-crews, .toggle-similar {
  display: none;
}
</style>
