<template>
  <div class="site-container" style="height: 100vh; max-width: 80%; margin: 0 auto; padding: 0; border: 1px solid red">
    <div class="navbar-containter" style="border: 1px solid red;">
      <nav class="navbar is-dark">
        <div class="navbar-brand">
          <router-link :to="{ name: 'home' }" class="navbar-item"><strong>Krypton</strong></router-link>
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="nav-bar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <router-link v-if="authenticated" :to="{ name: 'dashboard' }" class="navbar-item">Dashboard</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <!-- <LogoutComponent v-if="authenticated" @logoutConfirmed="handleLogout" :showLogoutCard="clickedLogout"/> -->
                <router-link v-if="!authenticated" :to="{ name: 'companySignup' }" class="button is-light">Signup</router-link>
                <button v-if="authenticated" class="button is-danger" @click="handleLogout()">Logout</button>
                <router-link v-if="!authenticated" :to="{ name: 'signin' }" class="button is-primary">Sign In</router-link>
                <span v-if="authenticated && username" class="navbar-item">Hello,&nbsp;  <strong>{{ username }}</strong></span>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>

    <div class="section" style="border: 1px solid red; padding: 0; margin: 0">
      <router-view />
    </div>
    <div>
      <p class="has-text-centered">Krypton Securities.pvt (c) since 2024</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState, mapActions } from 'vuex'; // Import for Vuex integration
import LogoutComponent from './components/LogoutComponent.vue';

export default {
  data() {
    return {
      showMobileMenu: false,
      clickedLogout: false,
    };
  },
  components: {
    LogoutComponent,
  },
  computed: {
    ...mapState(['authenticated', 'username', 'company_name']), // Map the authenticated state from the store
  },
  methods: {
    // ...mapActions(['logout']), // Use mapActions to access login action

    beforeCreate() {
      this.$store.commit('initializeAccount');
      const token = this.$store.state.token;

      if (token) {
        axios.defaults.headers.common['Authorization'] = "access_token " + token;
      } else {
        axios.defaults.headers.common['Authorization'] = "";
      }
    },
    clickedLogout() {
    this.clickedLogout = true; // Set clickedLogout to true on logout button click
  },
    handleLogout() {
      // Handle logout logic (e.g., clear local storage, dispatch logout action)
      this.$store.commit('removeToken')
      // Clear local storage (optional)
      localStorage.removeItem('access_token');
      localStorage.removeItem('username');
      localStorage.removeItem('company_name'); // Avoid storing password in local storage
      // Redirect to login page after logout
      this.$router.push({ name: 'home' });
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
