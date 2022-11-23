<template>
  <div id="app">
    <nav>
      <span v-if="isLogined()">
        <router-link :to="{ name: 'home' }">Home</router-link> |
        <router-link :to="{ name: 'recommend' }">Recommend</router-link> |
        <router-link :to="{ name: 'ProfileView' }">Profile</router-link> |
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'home' }">Home</router-link> |
        <router-link :to="{ name: 'recommend' }">Recommend</router-link> |
        <router-link :to="{ name: 'SignUpView' }">Sign Up</router-link> |
        <router-link :to="{ name: 'LoginView' }">Log In</router-link>
      </span>
    </nav>
    <router-view class="main-container" :key="$route.fullPath"/>
    <button @click="viewTop" class="top-btn">TOP</button>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      userName: null,
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("jwt");
      localStorage.removeItem("userName");
      this.$router.push({ name: "LoginView" });
    },
    isLogined() {
      this.userName = localStorage.getItem("userName");
      return localStorage.getItem("userName");
    },
    viewTop() {
      window.scrollTo({ left: 0, top: 0, behavior: "smooth" });
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
  width: 40vw;
  z-index: 100;
  margin-bottom: 100px;
  position: fixed;
  left: 0;
  top: 0;
  background-color: palevioletred;
  padding: 30px;
  padding-left: 60%;
}

nav a {
  font-weight: bold;
  color: azure;
}

nav a.router-link-exact-active {
  font-weight: bolder;
  color: #2c3e50;
}
.top-btn {
  position: fixed;
  right: 50px;
  top: 90vh;
  font-size: 24px;
}
</style>
