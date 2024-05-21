<template>
    <div class="section">
         <h1 class="title">Hello,&nbsp; <strong>{{company_name}}!</strong><br>Welcome to Krypton!</h1>
     <p>This is where you can view key metrics, reports, and other relevant information for your Krypton application.</p>
     <ul>
      <li></li>
      <li></li>
      <li></li>
     </ul>
    </div>
</template>


<script>
import axios from 'axios'
import { mapState }from 'vuex';
export default {
  computed: {
    ...mapState(['company_name']),
  }
  // No data or methods needed for this basic layout
};
</script>


