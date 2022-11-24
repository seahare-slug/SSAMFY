<template>
  <div>
    <h1>Home</h1>
    <hr />
    <HomeList />
  </div>
</template>

<script>
import HomeList from "../components/HomeList.vue";

export default {
  name: "HomeView",
  components: {
    HomeList,
  },
  created() {
    this.getMovies();
    this.getGenres();
    this.getUsers();
  },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies");
    },
    getGenres() {
      this.$store.dispatch("getGenres");
    },
    getUsers() {
      this.$store.dispatch("getUsers");
    }
  },
};
</script>
