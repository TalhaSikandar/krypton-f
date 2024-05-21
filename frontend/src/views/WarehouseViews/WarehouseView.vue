<template>
  <div class="Warehouse">
    <h1>Warehouses</h1>
    <div class="columns is-multiline">
      <div v-for="warehouse in warehouses" :key="warehouse.id" class="column is-half">
        <div class="card">
          <div class="card-header">
            <p class="card-header-title">
              {{ warehouse.company.company_name }} - {{ warehouse.id }}
            </p>
            <button class="button is-small" @click="openEditWarehouseModal(warehouse)">Edit</button>
          </div>
          <div class="card-content">
            <div class="content">
              <p v-if="warehouse.contact"><strong>Contact:</strong> {{ warehouse.contact }}</p>
              <p v-if="warehouse.address"><strong>Address:</strong> {{ warehouse.address }}</p>
              <div v-if="warehouse.products.length">
                <p><strong>Products:</strong></p>
                <ul>
                  <li v-for="product in warehouse.products" :key="product.product.id">
                    {{ product.product.product_name }} - Quantity: {{ product.quantity }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <button class="button is-primary" @click="openAddWarehouseModal">Add Warehouse</button>
    <generic-form-component
      v-if="showAddWarehouseModal"
      @close="closeAddWarehouseModal"
      @save="addWarehouse"
      :fields="warehouseFields"
      :form-data="editingWarehouse"
      form-title="Add Warehouse"
    ></generic-form-component>
    <generic-form-component
      v-if="showEditWarehouseModal"
      @close="closeEditWarehouseModal"
      @save="saveWarehouse"
      :fields="warehouseFields"
      :form-data="editingWarehouse"
      form-title="Edit Warehouse"
    ></generic-form-component>
  </div>
</template>

<script>
import GenericFormComponent from './GenericFormComponent.vue';
import axios from 'axios';
import store from '@/store'; // import your Vuex store

export default {
  name: 'WarehouseView',
  components: {
    GenericFormComponent
  },
  data() {
    return {
      warehouses: [],
      showAddWarehouseModal: false,
      showEditWarehouseModal: false,
      editingWarehouse: null,
      warehouseFields: {
        warehouse_name: { label: 'Name', type: 'text', placeholder: 'Warehouse Name' },
        contact: { label: 'Contact', type: 'text', placeholder: 'Contact' },
        address: { label: 'Address', type: 'text', placeholder: 'Address' },
      }
    };
  },
  mounted() {
    this.getWarehouses();
    document.title = 'Warehouses | Krypton';
  },
  methods: {
    getWarehouses() {
      axios
        .get('dashboard/warehouses/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          this.warehouses = response.data;
        })
        .catch(error => {
          console.error('Error fetching warehouses:', error);
        });
    },
    openAddWarehouseModal() {
      this.editingWarehouse= { company: '', contact: '', address: '', products: [] };
      this.showAddWarehouseModal = true;
    },
    closeAddWarehouseModal() {
      this.showAddWarehouseModal = false;
    },
    openEditWarehouseModal(warehouse) {
      this.editingWarehouse = { ...warehouse, products: warehouse.products || [] };
      this.showEditWarehouseModal = true;
    },
    closeEditWarehouseModal() {
      this.showEditWarehouseModal = false;
    },
    addWarehouse(newWarehouseData) {
      axios
        .post('dashboard/warehouses/', newWarehouseData, {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          this.warehouses.push(response.data);
          this.closeAddWarehouseModal();
        })
        .catch(error => {
          console.error('Error adding Warehouse:', error);
        });
    },
    saveWarehouse(updatedWarehouseData) {
      axios
        .put(`dashboard/warehouses/${updatedWarehouseData.id}/`, updatedWarehouseData, {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          const index = this.warehouses.findIndex(warehouse => warehouse.id === response.data.id);
          this.$set(this.warehouses, index, response.data);
          this.closeEditWarehouseModal();
        })
        .catch(error => {
          console.error('Error saving warehouse:', error);
        });
    }
  }
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
