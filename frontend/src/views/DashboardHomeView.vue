<template>
 <div class="home" style="border: 1px solid white; padding: 0; margin-top: 0">
<!--   <div class="columns" style="border: 1px solid white"> -->
   <div class="column is-narrow is-half-tablet is-one-quarter-desktop" >
    <aside class="menu is-dark" style="border: 1px solid white; min-height: 100%; margin-top: 0">
        <h1 v-if="company_name" class="title is-5 has-text-centered" style="padding: 0; margin: 0">{{ company_name }}</h1>
     <ul class="menu-list has-text-centered" style="border: 1px solid white">
                  <li><router-link class="has-text-centered" :to="{name: 'dashboardhome'}" exact :class="{ 'is-active': $route.name === 'dashboardhome' }" >Home</router-link></li>
                  <li><router-link class="has-text-centered" :to="{name: 'stores'}"exact :class="{ 'is-active': $route.name === 'stores' }">Stores</router-link></li>
                  <li><router-link class="has-text-centered" :to="{name: 'warehouses'}"  exact :class="{ 'is-active': $route.name === 'warehouses' }" >Warehouses</router-link></li>
                  <li><router-link class="has-text-centered" :to="{name: 'suppliers'}"  exact :class="{ 'is-active': $route.name === 'suppliers' }">Suppliers</router-link></li>
                  <li><router-link class="has-text-centered" :to="{name: 'employees'}"  exact :class="{ 'is-active': $route.name === 'employees' }"  >Employees</router-link></li>
                  <li><router-link class="has-text-centered" :to="{name: 'settings'}"  exact :class="{ 'is-active': $route.name === 'settings' }"  >Settings</router-link></li>
      </ul>
    </aside>
   </div>

   <div class="column is-flex is-flex-direction-column is-half-tablet is-three-quarters-desktop">
  <div class="section">
    <router-view/>
  </div>
   </div>
  </div>
<!--  </div> -->
</template>


<script>
import axios from 'axios';
import { mapState }from 'vuex';
export default {
  computed: {
    ...mapState(['company_name']),
  },

  mounted() {
    document.title = 'Dashboard | Krypton';
    this.$router.push({name: 'dashboardhome'}); // Replace with your dashboard route

  },
  // No data or methods needed for this basic layout
};
</script>

<style lang="scss">
@import '../../node_modules/bulma';

.home {
  display: flex;
  min-height: 100vh;
  padding: 0;
  margin: 0;
}

/* Optional styling for menu and content areas */
.menu {
  background-color: #2e333d !important;
  padding: 1rem;
}

.menu-list li {
  padding: 0.5rem 1rem;
}

.section {
  padding: 1rem 2rem;
}
</style>

