<template>
  <div id="app">
    <div class="default-background"></div>
    <div id="backgroundImg" class="back-img back-img-seung"></div>
    <nav>
      <router-link :to="{ name: 'home' }">
          <img class="logo" src="./img/SSAMFY.png" alt="logo"/>
        </router-link>
      <span @click="changeBackground" v-if="isLogined()">
        <router-link :to="{ name: 'home' }">Home</router-link> |
        <router-link :to="{ name: 'recommend' }">Recommend</router-link> |
        <router-link :to="{ name: 'ProfileView' }">Profile</router-link> |
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span @click="changeBackground" v-else>
        <router-link :to="{ name: 'home' }">Home</router-link> |
        <router-link :to="{ name: 'recommend' }">Recommend</router-link> |
        <router-link :to="{ name: 'SignUpView' }">Sign Up</router-link> |
        <router-link :to="{ name: 'LoginView' }">Log In</router-link>
      </span>
    </nav>
    <router-view class="main-container" :key="$route.fullPath" />
    <button @click="viewTop" class="top-btn common-btn">TOP</button>
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
    changeBackground() {
      const backgroundImg = document.querySelector("#backgroundImg");
      backgroundImg.classList.toggle("back-img-seung");
      backgroundImg.classList.toggle("back-img-song");
    },
  },
};
</script>

<style scoped>
#app {
  background-color: rgb(44, 44, 44);
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-width: 800px;
  min-height: 500px;
}
.default-background {
  z-index: -100;
  position: absolute;
  background-color: rgb(44, 44, 44);
  width: 100%;
  height: 100vh;
}
.back-img {
  position: fixed;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100%;
  background-repeat: no-repeat;
}
.back-img-seung {
  background-image: url("./img/seungkyu_back.png");
}
.back-img-song {
  background-image: url("./img/songsub_back.png");
  background-size: 30% 100%;
}
nav {
  position: fixed;
  display: flex;
  justify-content: space-between;
  background-color: rgb(209, 132, 158);
  top: 0;
  left: 0;
  width: 90vw;
  margin-bottom: 100px;
  padding: 30px 10vw 10px 0;
  z-index: 100;
  border-bottom: 2px solid black;
}
nav a {
  color: azure;
  font-weight: bold;
}

nav a.router-link-exact-active {
  color: #2c3e50;
  font-weight: bolder;
}
.top-btn {
  position: fixed;
  right: 50px;
  top: 90vh;
  font-size: 18px;
}
.logo {
  width: 70px;
  margin-left: 50px;
}
</style>
