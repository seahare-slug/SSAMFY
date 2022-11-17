import axios from "axios";
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movies: [],
    genres: [],
    userName: [],
    token: null,
  },
  getters: {},
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies;
    },
    GET_GENRES(state, res) {
      state.genres = res;
    },
    USER_NAME(state, userName) {
      state.userName = userName;
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          context.commit("GET_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getGenres(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/genres/`,
      }).then((res) => {
        context.commit("GET_GENRES", res.data);
      });
    },
    userName(context, userName) {
      context.commit("USER_NAME", userName);
    },
  },
  modules: {},
});
