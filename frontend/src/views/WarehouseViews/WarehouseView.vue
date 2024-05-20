<template>
  <div class="stores">
    <h1>Suppliers</h1>
    <div class="columns is-multiline">
      <div v-for="store in stores" :key="store.id" class="column is-one-third">
        <div class="card">
          <div class="card-header">
            <p class="card-header-title">
              {{ store.company }} - {{ store.id }}
            </p>
          </div>
          <div class="card-content">
            <div class="content">
              <p>
                <strong>Manager:</strong> {{ store.manager }}
              </p>
              <p>
                <strong>Contact:</strong> {{ store.contact }}
              </p>
              <p>
                <strong>Address:</strong> {{ store.address }}
              </p>
              <p>
                <strong>Updated at:</strong> {{ store.updated_at | formatDate }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
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
    document.title = 'My Warehouses'
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

