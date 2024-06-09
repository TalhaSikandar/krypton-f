<template>
  <div class="dashboard-content-container">
    <h1>Stores</h1>
    <div class="columns is-multiline">
      <div v-for="(store, index) in paginatedStores" :key="store.id" class="column is-4">
        <div class="card">
          <div class="card-header">
            <p class="card-header-title">
              Store - {{ store.id }}
            </p>
            <button class="button edit-button is-small" @click="openEditStoreModal(store)">Edit</button>
          </div>
          <div class="card-content">
            <div class="content">
              <p><strong>Manager:</strong> {{ store.manager.email }}</p>
              <p v-if="store.contact"><strong>Contact:</strong> {{ store.contact }}</p>
              <p v-if="store.address"><strong>Address:</strong> {{ store.address }}</p>
              <button class="button edit-button is-small" @click="openEditStoreModalProducts(store)">View Products</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <nav class="pagination is-centered" role="navigation" aria-label="pagination">
      <button class="button pagination-previous" @click="previousPage" :disabled="currentPage === 1">Previous</button>
      <button class="button pagination-next" @click="nextPage" :disabled="currentPage >= totalPages">Next</button>
    </nav>
    <p v-if="!this.stores.length">You have got no Stores, Kindly Add!</p>
    <button @click="openAddStoreModal" class="button add-store" style="background-color: var(--primary-color); color: var(--text-color)">Add Store</button>

    <save-store-view
      v-if="showAddStoreModal"
      @close="closeAddStoreModal"
      @save="addStore"
      :newStore="newStoreData"
    ></save-store-view>

    <edit-store-products
      v-if="showEditStoreModalProducts"
      @close="closeEditStoreModalProducts"
      @save="saveStore"
      :store_Id="store_id"
    ></edit-store-products>

    <edit-store-view
      v-if="showEditStoreModal"
      :storeId="currentStore"
      @close="closeEditStoreModal"
      @save="saveStore"
    ></edit-store-view>
  </div>
</template>

<script>
import saveStoreView from './saveStoreView.vue';
import EditStoreView from './EditStoreView.vue';
import EditStoreProducts from './EditStoreProducts.vue';
import { toast } from 'bulma-toast';
import axios from 'axios';
import store from '@/store'; // import your Vuex store

export default {
  name: 'StoreView',
  components: {
    saveStoreView,
    EditStoreProducts,
    EditStoreView,
  },
  computed: {
    // Calculate total number of pages based on stores and items per page
    totalPages() {
      return Math.ceil(this.stores.length)*6; // Change '2' to adjust items per page
    },

    // Paginate the stores based on current page
    paginatedStores() {
      const start = (this.currentPage - 1)*6 ; // Change '2' to adjust items per page
      const end = start + 6; // Change '2' to adjust items per page
      return this.stores.slice(start, end);
    }
  },
  data() {
    return {
      currentPage: 1,
      stores: [],
      showAddStoreModal: false,
      showEditStoreModal: false,
      showEditStoreModalProducts: false,
      editingStore: null,
      store_id: '',
      newStoreData: {
        contact: {
          contact_no: '',
          email: '',
        },
        address: {
          city: '',
          country: '',
        },
        manager_password: '',
      },
      currentStore: null,
    };
  },
  mounted() {
    this.getStores();
    document.title = 'Stores | Krypton'
  },
  methods: {
    getStores() {
      axios
        .get('dashboard/stores/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          this.stores = response.data;
          if(this.stores)
            console.log("Stores", this.stores);
        })
        .catch(error => {
          console.error('Error fetching stores:', error);
        });
    },
    openAddStoreModal() {
      this.editingStore = { company: '', manager: '', contact: '', address: '', manager_password: '', products: [] };
      this.showAddStoreModal = true;
    },
    closeAddStoreModal() {
      this.showAddStoreModal = false;
    },
    openEditStoreModal(store) {
      this.currentStore = store.id;
      this.editingStore = { ...store, manager_password: '', products: store.products || [] , id: store.id};
      this.showEditStoreModal = true;
    },
    closeEditStoreModal() {
      this.showEditStoreModal = false;
    },
    openEditStoreModalProducts(store) {
      this.store_id = store.id; 
      console.log("id", this.store_id)
      this.showEditStoreModalProducts = true;
    },
    closeEditStoreModalProducts() {
      this.showEditStoreModalProducts = false;
    },
    addStore(newStoreData) {
      console.log(newStoreData);
      axios
        .post('dashboard/stores/', newStoreData, {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          this.stores.push(response.data);
          this.closeAddStoreModal();
          toast({
            message: 'Store added successfully',
            type: 'is-success',
            duration: 5000,
          });
        })
        .catch(error => {
          toast({
            message: 'Error adding store: ' + error.response.data.error || 'Unknown error',
            type: 'is-danger',
            duration: 5000,
          });
          console.error('Error adding store:', error);
        });
    },
    saveStore(updatedStoreData) {
      axios
        .put(`dashboard/stores/${updatedStoreData.id}/`, updatedStoreData, {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          const index = this.stores.findIndex(store => store.id === response.data.id);
          this.$set(this.stores, index, response.data);
          this.closeEditStoreModal();
          toast({
            message: 'Store updated successfully',
            type: 'is-success',
            duration: 5000,
          });
        })
        .catch(error => {
          console.error('Error saving store:', error);
          toast({
            message: 'Error saving store: ' + error.response.data.error || 'Unknown error',
            type: 'is-danger',
            duration: 5000,
          });
        });
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },

    // Switch to next page
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
  },
};
</script>

