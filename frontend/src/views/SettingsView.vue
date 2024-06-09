<template>
  <div>
    <h2>Welcome to Settings</h2>
    <button class="company_delete" @click="deleteCompany()">Delete Company</button>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store';
import { mapState } from 'vuex';

export default {
  methods: {
    async deleteCompany() {
      try {
        const companyId = store.state.company_id; // Replace 'your_company_id' with the actual company ID
        console.log("doing it", store.state.company_id);
        if(companyId){
          const response = await axios.delete(`companies/${companyId}/`,{
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
          });
          console.log('Company deleted:', response.data);
          this.$store.commit('removeToken')
          // Clear local storage (optional)
          localStorage.removeItem('access_token');
          localStorage.removeItem('username');
          localStorage.removeItem('company_name'); // Avoid storing password in local storage
          // Redirect to login page after logout
          this.$router.push({ name: 'home' });
        }
        // Redirect or handle success message as needed
      } catch (error) {
        console.error('Error deleting company:', error.response.data);
        // Handle error and show appropriate message to the user
      }
    },
  },
};
</script>

<style lang="scss">
@import '../../node_modules/bulma';
.company_delete {
  background-color: red;
  color: var(--text-color);
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

</style>

