<template>
  <div class="stores">
    <h1>Stores</h1>
    <div class="columns is-multiline">
      <div v-for="store in stores" :key="store.id" class="column is-half">
        <div class="card">
          <div class="card-header">
            <!-- <p class="card-header-title"> -->
            <!--   {{ store.company.company_name }} - {{ store.id }} -->
            <!-- </p> -->
            <p class="card-header-title">
              Store - {{ store.id }}
            </p>
            <button class="button is-small" @click="openEditStoreModal(store)">Edit</button>
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

    <button class="button is-primary" @click="openAddStoreModal">Add Store</button>
    <!-- adding store -->
    <generic-form-component
      v-if="showAddStoreModal"
      @close="closeAddStoreModal"
      @save="addStore"
      :fields="storeFields"
      :form-data="editingStore"
      form-title="Add Store"
    ></generic-form-component>
    <!-- editing store -->
    <edit-store-view
      v-if="showEditStoreModal"
      :storeId="currentStore"
      @close="closeEditStoreModal"
      @save="saveStore"
    ></edit-store-view>
  </div>
</template>

<script>
import GenericFormComponent from './GenericFormComponent.vue';
import EditStoreView from './EditStoreView.vue';
import axios from 'axios';
import store from '@/store'; // import your Vuex store

export default {
  name: 'StoreView',
  components: {
    GenericFormComponent,
    EditStoreView,
  },
  data() {
    return {
      stores: [],
      showAddStoreModal: false,
      showEditStoreModal: false,
      editingStore: null,
      storeFields: {
        contact: { label: 'Contact', type: 'text', placeholder: 'Contact' },
        address: { label: 'Address', type: 'text', placeholder: 'Address' },
        manager_password: { label: 'Manager Password', type: 'password', placeholder: 'Password' }
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

<style scoped>
/* Add any custom styles if needed */
</style>
