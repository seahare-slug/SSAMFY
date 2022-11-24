<template>
  <div class="wrap-recommend">
    <div class="movie-filter">
      <div class="common-btn" @click="bringLike">좋아요 기반 다시 추천받기</div>
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
    <div v-if="!username">
      <div
        class ="recommend-text"
      >로그인이 필요한 페이지입니다.
      </div>
      <img src="../img/SSAMFY.png" alt="ssamfy-logo" class ="recommend-img">
    </div>
    <div class="wrap-recommend-list">
      <RecommendListItem
        v-for="movie in algoList"
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
import _ from "lodash";
export default {
  name: "RecommendList",
  components: {
    RecommendListItem,
  },
  data() {
    return {
      username: localStorage.getItem("userName"),
      isClassic: false,
      isIndependent: false,
      like_genres: [],
      movie_genres: {
        28: 5, // 액션
        12: 5, // 모험
        16: 5, // 애니메이션
        35: 5, // 코미디
        80: 5, // 범죄
        99: 5, // 다큐멘터리
        18: 5, // 드라마
        10751: 5, // 가족
        14: 5, // 판타지
        36: 5, // 역사
        27: 5, // 공포
        10402: 5, // 음악
        9648: 5, // 미스터리
        10749: 5, // 로맨스
        878: 5, // SF
        10770: 5, // TV 영화
        53: 5, // 스릴러
        10752: 5, // 전쟁
        37: 5, // 서부
      },
      likeList: [],
      algoList: [],
    };
  },
  created() {
    this.bringLike();
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
      this.algoList = [];
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/liked/${this.username}/`,
      })
        .then((res) => {
          this.likeList = res.data.liked_movie;
          // liketList에 해당하는 각각의 장르들을 저장(like_genres)
          for (const movie of this.movies) {
            if (this.likeList.includes(movie.id)) {
              this.like_genres.push(...movie.genre_ids);
            }
          }
          // 여기서 포문을 돌려 전체 장르(movie_genres)에서 좋아하는 장르(likeList.movie.genre_ids)에 점수를 주고싶음.
          for (const like_genre of this.like_genres) {
            this.movie_genres[like_genre] += 5;
          }
          // 그 점수를 기반으로 새로운 리스트 정렬한 기준 완성.
          let movieScore = -1;
          for (const movie of this.movies) {
            movieScore = 0;
            for (const genreId of movie.genre_ids) {
              movieScore += this.movie_genres[genreId];
            }
            movieScore = parseInt(movieScore / movie.genre_ids.length);
            this.algoList.push({
              movieScore: movieScore,
              id: movie.id,
              title: movie.title,
              poster_path: movie.poster_path,
              release_date: movie.release_date,
              vote_average: movie.vote_average,
              vote_count: movie.vote_count,
            });
          }
          this.algoList.sort((a, b) => b["movieScore"] - a["movieScore"]);
          this.algoList = _.sampleSize(this.algoList.slice(0, 300), 100);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.wrap-recommend-list {
  margin: 0 auto;
  display: flex;
  flex-flow: row wrap;
}
.movie-filter {
  margin-bottom: 30px;
  display: flex;
  flex-direction: row-reverse;
}
.movie-filter div {
  margin: 5px;
}
.recommend-img {
  width: 70%;
  height: 70%;
}
.recommend-text{
  color: azure;
  font-size: 20px;
}
</style>
