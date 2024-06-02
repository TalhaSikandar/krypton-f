<template>
  <div class="dashboard-content-container">
    <h1>Stores</h1>
    <div class="columns is-multiline">
      <div v-for="store in stores" :key="store.id" class="column is-4">
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
              <div v-if="store.products.length">
                <p><strong>Products:</strong></p>
                <ul>
                  <li v-for="product in store.products" :key="product.product.id">
                    {{ product.product.product_name }} - Quantity: {{ product.quantity }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <p v-if="!this.stores.length">You have got no Stores, Kindly Add!</p>
    <button @click="openAddStoreModal" class="button add-store" style="background-color: var(--primary-color); color: var(--text-color)">Add Store</button>

    <save-store-view
      v-if="showAddStoreModal"
      @close="closeAddStoreModal"
      @save="addStore"
      :newStore="newStoreData"
    ></save-store-view>

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
import axios from 'axios';
import store from '@/store'; // import your Vuex store

export default {
  name: 'StoreView',
  components: {
    saveStoreView,
    EditStoreView,
  },
  data() {
    return {
      stores: [],
      showAddStoreModal: false,
      showEditStoreModal: false,
      editingStore: null,
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
        })
        .catch(error => {
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
        })
        .catch(error => {
          console.error('Error saving store:', error);
        });
    }
  }
};
</script>

