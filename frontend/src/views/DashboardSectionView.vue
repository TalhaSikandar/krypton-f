<template>
    <div class="section">
     <h1 class="title">Welcome to Krypton!</h1>
     <p>This is where you can view key metrics, reports, and other relevant information for your Krypton application.</p>
     <ul>
      <li>List item 1</li>
      <li>List item 2</li>
      <li>List item 3</li>
     </ul>
    </div>
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

