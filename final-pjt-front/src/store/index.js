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
    comments: [],
    users: [],
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
    GET_COMMENTS(state, comments) {
      state.comments = comments;
    },
    GET_USERS(state, users) {
      state.users = users;
    }
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
    getComments(context, comments) {
      context.commit("GET_COMMENTS", comments);
    },
    getUsers(context) {
      axios({
        method: "get",
        url: `${API_URL}/accounts/users/`,
      }).then((res) => {
        context.commit("GET_USERS", res.data);
        console.log(res.data)
      });
    }
  },
  modules: {},
});
