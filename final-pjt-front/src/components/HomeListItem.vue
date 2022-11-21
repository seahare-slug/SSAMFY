<template>
  <div class="wrap-home-item movie-card">
    <h4>{{ movie.title }}</h4>
    <img
      class="poster-img"
      :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
      alt="movie_poster"
    />
    <span @click="toggleLike" class="like" :class="{ 'is-liked': !isLiked }"
      >🤍</span
    >
    <span @click="toggleLike" class="like" :class="{ 'is-liked': isLiked }"
      >🧡</span
    >
    <div>
      <router-link
        class="common-btn"
        :to="{ name: 'DetailView', params: { id: movie.id } }"
        >DETAIL</router-link
      >
    </div>
  </div>
</template>

<script>
// import axios from 'axios';

export default {
  name: "HomeListItem",
  data() {
    return {
      isLiked: false,
      likedData: {
        liked_movie_id: this.movie.id,
        username: localStorage.getItem("userName"),
      }
    };
  },
  props: {
    movie: Object,
  },
  computed: {
  },
  methods: {
    toggleLike() {
      this.isLiked = !this.isLiked;
      // axios({
      //   method: "post",
      //   url: "http://127.0.0.1:8000/accounts/profile/liked/",
      //   data: {
      //     likedData: this.likedData,
      //   }
      // })
      //   .then(() => {
      //     console.log("~~~~좋아요 했는지 보냅니다~~~~")
      //   })
    },
  },
};
</script>

<style scoped>
.wrap-home-item {
  position: relative;
  width: 20%;
  height: 50vh;
  margin: 5px;
}
.poster-img {
  height: 70%;
}

.like {
  cursor: pointer;
  font-size: 48px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: none;
  opacity: 0;
}
.is-liked {
  display: block !important;
}
.like:hover {
  opacity: 1;
}
img:hover ~ .like {
  opacity: 1;
}
</style>
