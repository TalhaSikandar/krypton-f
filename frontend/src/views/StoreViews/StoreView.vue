<template>
  <div class="stores">
    <h1>Stores</h1>
    <div class="columns is-multiline">
      <div v-for="store in stores" :key="store.id" class="column is-4">
        <div class="card">
          <div class="card-header">
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

    <p v-if="!this.stores.length">You have got no Stores, Kindly Add!</p>
    <button @click="openAddStoreModal" class="button add-store" style="background-color: var(--primary-color); color: var(--text-color)">Add Store</button>

    <generic-form-component
      v-if="showAddStoreModal"
      @close="closeAddStoreModal"
      @save="addStore"
      :fields="storeFields"
      :form-data="editingStore"
      form-title="Add Store"
    ></generic-form-component>

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
.stores {
  background-color: var(--background-color);
  color: var(--text-color);
  padding: 1rem;
}

.columns {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.column {
  flex: 0 0 25%;
  max-width: 24%;
}

.card {
  background-color: #f5f5f5; /* Light gray background for cards */
  border: 1px solid var(--border-color);
  border-radius: 4px;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle box shadow for cards */
  margin-bottom: 1rem;
  box-shadow: 1px 19px 35px -3px rgba(0,0,0,0.75);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border-color);
}

.card-header-title {
  font-weight: bold;
  color: var(--text-black-color);
}

.card-content {
  padding-top: 1rem;
  color: var(--text-black-color);
}

.content {
  line-height: 1.5; /* Adjust line height for better readability */
  color: var(--text-black-color);
}

strong {
  color: var(--text-black-color);
}

.button {
  background-color: var(--primary-color);
  color: var(--text-color);
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.button.add-store {
  box-shadow: 1px 19px 35px -3px rgba(0,0,0,0.75);
}
.button:hover {
  opacity: 0.5;
}
</style>
