<template>
  <div>
    <div
      class="wrap-recommand-item movie-card"
      v-if="
        isClassic === true &&
        movie.release_date.slice(0, 4) < 2022 &&
        movie.vote_average > 7.5 &&
        isIndependent === true &&
        50 < movie.vote_count &&
        movie.vote_count < 200 &&
        movie.vote_average > 7
      "
    >
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
    <div
      class="movie-card wrap-recommand-item"
      v-else-if="
        isClassic === false &&
        isIndependent === true &&
        50 < movie.vote_count &&
        movie.vote_count < 200 &&
        movie.vote_average > 7
      "
    >
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
    <div
      class="movie-card wrap-recommand-item"
      v-else-if="
        isClassic === true &&
        movie.release_date.slice(0, 4) < 2022 &&
        movie.vote_average > 7.5 &&
        isIndependent === false
      "
    >
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
    <div
      class="movie-card wrap-recommand-item"
      v-else-if="isClassic === false && isIndependent === false"
    >
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
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "RecommendListItem",
  data() {
    return {
      isLiked: false,
      username: localStorage.getItem("userName"),
    };
  },
  props: {
    movie: Object,
    isClassic: Boolean,
    isIndependent: Boolean,
  },
  created() {
    this.setLike()
  },
  methods: {
    toggleLike() {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/accounts/liked/${this.movie.id}/`,
        data: {
          username: this.username,
        }
      })
        .then(() => {
          this.isLiked = !this.isLiked;
        })
        .catch((err) => {
          console.log(err)
        })
    },
    setLike() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/liked/${this.username}/`,
      })
        .then((res) => {
          this.isLiked = res.data.liked_movie.includes(this.movie.id)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
};
</script>

<style scoped>
.wrap-recommand-item {
  position: relative;
  width: 300px;
  height: 50vh;
  margin: 6px;
}
.poster-img {
  height: 75%;
  width: 90%;
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
