<template>
  <div>
    <h1>{{ credentials.username }} 님의 프로필</h1>
    <div class="wrap-profile-content">
      <div class="user-comments">
        <h2>최근 본 영화 댓글</h2>
        <div v-for="movie in movies"
          :key="movie.id">
          <div v-if="comments.length !== 0">
            <div class="movie-title" v-if="comments[0].movie === movie.id">
              <h2>{{ movie.title }}</h2>
            </div>
          </div>
        </div>
        <div class="wrap-comment" v-for="comment in comments"
        :key="comment.username"
        >
          <h3>"{{ comment.content }}"</h3>
          <h5>{{ comment.created_at.slice(0, 10) }}</h5>
        </div>
      </div>
      <div class="user-likes">
        <h1>좋아요한 영화</h1>
        <div class="wrap-like-movie">
          <div
            v-for="movie in movies"
            :key="movie.id">
            <div
              class="like-movie movie-card"
              v-if="likeList.includes(movie.id)">
              <img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" alt="movie">
              <div>
                <router-link
                  class="common-btn"
                  :to="{ name: 'DetailView', params: { id: movie.id } }"
                  >DETAIL</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  data() {
    return {
      credentials: {
        username: localStorage.getItem("userName"),
      },
      likeList: [],
    };
  },
  computed:{
    comments(){
      return this.$store.state.comments
    },
    movies() {
        return this.$store.state.movies;
      },
  },
  created() {
    this.bringLike()
  },
  methods: {
    bringLike() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/liked/${this.credentials.username}/`,
      })
        .then((res) => {
          this.likeList = res.data.liked_movie
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
};
</script>

<style scoped>
.movie-title {
  margin: 20px;
  font-size: 36px;
  font-weight: bolder;
}
.content {
  padding: 10px;
  background-color: rgba(216, 112, 147, 0.3);
}
.user-comments {
  width: 30%;
}
.user-likes {
  width: 55%;
}
.wrap-comment {
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  border: solid pink 2px;
  padding: 0 5%;
}
.wrap-profile-content {
  display: flex;
  justify-content: space-around;
  flex: 1 1 auto;
}
.wrap-like-movie {
  background-color: rgba(216, 112, 147, 0.3);
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  border: 2px black solid;
  border-radius: 20px;
}
.like-movie {
  background-color: azure;
  position: relative;
  padding: 10px;
  width: 7vw;
  height: 12vw;
  margin: 6px;
}
.like-movie img {
  height: 85%;
  width: 90%;
}
</style>
