import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [
      {
        id:1,
        title: '제목1',
        content : '내용1',
      },
      {
        id:2,
        title: '제목2',
        content : '내용2',
      },

    ]
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
