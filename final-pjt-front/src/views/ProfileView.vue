<template>
  <div>
    <h1>{{ credentials.username }} 님의 프로필</h1>
    <div class="wrap-profile-content">
      <div class="user-comments">
        <h2>최근 작성한 영화 댓글</h2>
        <div v-for="movie in movies"
          :key="movie.id">
          <div v-if="comments.length !== 0">
            <div class="movie-title" v-if="comments[0].movie === movie.id">
              {{ movie.title }}
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
      <div>
        <h1>좋아요한 영화</h1>
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
    axios({
      method: "post",
      url: "http://127.0.0.1:8000/accounts/profile/",
      data: this.credentials,
    })
      .then(() => {
      })
      .catch((err) => {
        console.log(err);
      });
  },
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
.wrap-comment {
  width: 90%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  border: solid pink 2px;
  padding: 0 5%;
}
.wrap-profile-content {
  display: flex;
  justify-content: space-around;
}
</style>
