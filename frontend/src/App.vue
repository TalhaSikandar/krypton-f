<template>
  <div class="site-container">
    <div class="navbar-containter" >
      <nav class="navbar is-dark">
        <div class="navbar-brand">
          <router-link :to="{ name: 'home' }" class="navbar-item company-logo"><strong>K R Y P T O N</strong></router-link>
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="nav-bar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">

            <div class="navbar-item">
              <div class="nav-bar-btns">
                <!-- <LogoutComponent v-if="authenticated" @logoutConfirmed="handleLogout" :showLogoutCard="clickedLogout"/> -->
                <router-link v-if="authenticated" :to="{ name: 'dashboard' }" class="navbar-item">Dashboard</router-link>
                <router-link v-if="!authenticated" :to="{ name: 'companySignup' }" class="signup">Signup</router-link>
                <div  v-if="authenticated" class="nav-bar-btn logout">
                <div @click="handleLogout()">Logout</div>
                </div>
                <div  v-if="!authenticated" class="nav-bar-btn signin">
                <router-link :to="{ name: 'signin' }" >Sign in</router-link>
                </div>
                <span v-if="authenticated && username" class="navbar-item">Hello,&nbsp;  <strong style="color: var(--accent-color)">{{ username }}</strong></span>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>

      <router-view style="height: 92vh; padding: 0"/>
    <div>
      <p class="has-text-centered">© All rights reserved, Krypton inc. 2024</p>
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
  mounted() {
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
<style>
 @import "./main"
/*Global Styles */
/* Optional: Adjust content width if needed */
.site-container {
  width: 100%; /* Adjust content width for responsiveness */
  background-color: var(--background-color,#232336); /* Dark background color */
  color: var(--white-color); /* Light text color */
  display: flex; /* Make it a flex container for vertical layout */
  flex-direction: column; /* Stack elements vertically */
  min-height: 100vh; /* Set minimum height for full viewport */
}

.navbar-containter {
  border: none; /* Remove red border */
  background-color: var(--background-color,#232336); /* Match dark background */
  padding: 0rem 0rem; /* Add some padding */
}

.company-logo {
   font-size: 1.2rem;
 }

.navbar {
  background-color: #232336; /* Match dark background */
  border: none; /* Remove default border */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Subtle box shadow for navbar */
}

.navbar-brand {
  color: #ffffff; /* Light text for brand name */
}

.navbar-item {
  color: #ffffff; /* Light text for menu items */
  padding: 0.5rem 1rem; /* Adjust padding for spacing */
}

.navbar-item a,
.navbar-item router-link .nav-bar-btn {
  color: inherit; /* Inherit text color from parent */
  text-decoration: none; /* Remove underline */
  transition: color 0.3s ease; /* Smooth color transition on hover */
}

.nav-bar-btn :hover,
.navbar-item a:hover,
.navbar-item router-link:hover{
  color: #9d4edd; /* Optional accent color on hover */
}

.navbar-burger {
  background-color: #ffffff; /* Light color for burger menu icon */
  border: none; /* Remove default border */
}

.navbar-burger span {
  background-color: #ffffff; /* Light color for burger menu lines */
}

.navbar-menu {
  background-color: #232336; /* Match dark background */
}

.navbar-end {
  justify-content: flex-end; /* Align right-side elements */
}


.nav-bar-btn.logout {
  /* Adjust color for danger button (optional) */
  border-color: #ff0000; /* Red border */
}

.button.is-danger:hover {
  background-color: rgba(255, 0, 0, 0.1); /* Slight red background on hover */
}

.has-text-centered {
  color: #ffffff; /* Light text for copyright */
  margin-top: 1rem; /* Add some margin above copyright */
}
.btn {
  display: flex;
  gap: 8px;
}

.nav-bar-btns {
  display:flex;
  gap: 2rem;
  margin-right: 2rem;
}

.logout {
  margin-top: 6px;
}
</style>
