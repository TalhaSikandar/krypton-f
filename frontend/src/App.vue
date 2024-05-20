<template>
  <div class="site-container" style="max-width: 80%; margin: 0 auto">
    <div class="navbar-containter">
      <nav class="navbar is-dark">
        <div class="navbar-brand">
          <router-link :to="{name: 'home'}" class="navbar-item"><strong>Krypton</strong></router-link>
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="nav-bar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link v-if="!authenticated" :to="{name: 'companySignup' }" class="button is-light">Signup</router-link>
                <router-link v-if="authenticated" @click="logout()" class="button is-danger">Logout</router-link>
                <router-link v-if="!authenticated" :to="{name: 'signin' }" class="button is-primary">Sign In</router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>

    <div class="section">
      <router-view/>
    </div>

    <footer class="footer">
      <p class="has-text-centered">Krypton Securities since 2024</p>
    </footer>
  </div>
</template>


<script>
import axios from 'axios';
import { mapState, mapActions } from 'vuex'; // Import for Vuex integration

export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },
  computed: {
    ...mapState(['authenticated']), // Map the authenticated state from the store
  },
  methods: {

    ...mapActions(['logout']), // Use mapActions to access login action


    logout() {
        axios.defaults.headers.common['Authorization'] = "";

        localStorage.removeItem("access_token")
        localStorage.removeItem("username")
        localStorage.removeItem("password")

        this.$store.commit('removeToken')
    },

    beforeCreate() {
      this.$store.commit('initializeAccount');
      const token = this.$store.state.token;
      
      if (token) {
        axios.defaults.headers.common['Authorization'] = "access_token" + token;
      } else {
        axios.defaults.headers.common['Authorization'] = "";
      }

    },
  },
};
</script>

<style lang="scss">
@import '../node_modules/bulma';
/* Global Styles */
html, body {
  overflow-x: hidden !important; /* Prevent horizontal scroll on all pages */
}

/* Optional: Adjust content width if needed */
.site-container {
  width: 100%; /* Adjust content width for responsiveness */
}
</style>
