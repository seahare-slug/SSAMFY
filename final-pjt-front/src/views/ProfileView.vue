<template>
  <div>
    <h1>{{ credentials.username }}님의 프로필</h1>
    <h2>최신 영화 댓글</h2>
    <p v-for="comment in comments"
    :key="comment.username"
    >
    {{comment.content}}
    </p>
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
        console.log("프로필 교신성공!");
        console.log(this.comments)
      })
      .catch((err) => {
        console.log(err);
      });
      
  },
};
</script>

<style></style>
