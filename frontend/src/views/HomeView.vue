<template>
  <div>Home</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'StoresView',
  data() {
    return {
      stores: [],
    };
  },
  mounted() {
    this.getStores();
    document.title = 'Home | Krypton'
  },
  methods: {
    getStores() {
      axios
        .get('dashboard/stores/')
        .then(response => {
          this.stores = response.data;
        })
        .catch(error => {
          console.error('Error fetching stores:', error);
        });
    },
    formatDate(dateString) {
      // Implement date formatting logic based on your requirements (e.g., using moment.js or a similar library)
      return new Date(dateString).toLocaleDateString(); // Example using built-in Date object
    },
  },
};
</script>

<style scoped>
.stores {
  /* Add your custom styles for the overall stores section */
}

.card {
  /* Style the card elements */
}

.card-header-title {
  /* Style the card header title */
}

.content {
  /* Style the content area within the card */
}
</style>

