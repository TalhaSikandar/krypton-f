<template>
 <div class="home" style="border: 1px solid red">
<!--   <div class="columns" style="border: 1px solid red"> -->
   <div class="column is-narrow is-half-tablet is-one-quarter-desktop" style="border: 1px solid red">
    <aside class="menu">
     <ul class="menu-list">
                  <li><router-link :to="{name: 'dashboardhome'}">Home</router-link></li>
                  <li><router-link :to="{name: 'stores'}">Stores</router-link></li>
                  <li><router-link :to="{name: 'warehouses'}">Warehouses</router-link></li>
                  <li><router-link :to="{name: 'suppliers'}">Suppliers</router-link></li>
                  <li><router-link :to="{name: 'employees'}">Employees</router-link></li>
                  <li><router-link :to="{name: 'settings'}">Settings</router-link></li>
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
import axios from 'axios'
export default {
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
  background-color: #f5f5f5;
  padding: 1rem;
}

.menu-list li {
  padding: 0.5rem 1rem;
}

.section {
  padding: 1rem 2rem;
}
</style>

