<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'recommend' }">Recommend</router-link> |
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> |
      <router-link :to="{ name: 'LoginView' }">LoginPage</router-link> |
      <router-link :to="{ name: 'ProfileView' }">Profile</router-link> |
      <router-link @click.native="logout" to="#">Logout</router-link>
    </nav>
    <router-view class="main-container" />
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    logout() {
      localStorage.removeItem("jwt");
      localStorage.removeItem("userName");
      console.log("로그아웃 됨!");
    },
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  background-color: palevioletred;
  padding: 30px;
  padding-left: 60%;
}

nav a {
  font-weight: bold;
  color: rgb(250, 250, 250);
  text-shadow: -1px 0 #2c3e50, 0 1px #2c3e50, 1px 0 #2c3e50, 0 -1px #2c3e50;
}

nav a.router-link-exact-active {
  font-weight: 900;
  color: #2c3e50;
  text-shadow: none;
}
</style>
