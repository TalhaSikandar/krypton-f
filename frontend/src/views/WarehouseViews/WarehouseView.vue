<template>
  <div class="dashboard-content-container">
    <h1>Warehouses</h1>
    <div class="columns is-multiline">
      <div v-for="warehouse in warehouses" :key="warehouse.id" class="column is-half">
        <div class="card">
          <div class="card-header">
            <p class="card-header-title">
              Warehouse - {{ warehouse.id }}
            </p>
            <button class="button edit-button is-small" @click="openEditWarehouseModal(warehouse)">Edit</button>
          </div>
          <div class="card-content">
            <div class="content">
              <p v-if="warehouse.contact"><strong>Contact:</strong> {{ warehouse.contact }}</p>
              <p v-if="warehouse.address"><strong>Address:</strong> {{ warehouse.address }}</p>
              <!-- <div v-if="warehouse.products.length"> -->
              <!--   <p><strong>Products:</strong></p> -->
              <!--   <ul> -->
              <!--     <li v-for="product in warehouse.products" :key="product.product.id"> -->
              <!--       {{ product.product.product_name }} - Quantity: {{ product.quantity }} -->
              <!--     </li> -->
              <!--   </ul> -->
              <!-- </div> -->
            <button class="button edit-button is-small" @click="openEditWarehouseModalProducts(warehouse)">Products</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <p v-if="!this.warehouses.length">You have got no Stores, Kindly Add!</p>
    <button class="button is-primary" @click="openAddWarehouseModal">Add Warehouse</button>
    <save-warehouse-view
      v-if="showAddWarehouseModal"
      @close="closeAddWarehouseModal"
      @save="addWarehouse"
    ></save-warehouse-view>
    <edit-warehouse-view
      v-if="showEditWarehouseModal"
      @close="closeEditWarehouseModal"
      @save="saveWarehouse"
      :fields="warehouseFields"
      :form-data="editingWarehouse"
    ></edit-warehouse-view>
    <edit-warehouse-products-view
      v-if="showEditWarehouseModalProducts"
      @close="closeEditWarehouseModalProducts"
      @save="saveWarehouse"
      :warehouse_id="warehouse_id"
    ></edit-warehouse-products-view>
  </div>
</template>

<script>
import EditWarehouseView from './EditWarehouseView.vue';
import SaveWarehouseView from './SaveWarehouseView.vue';
import EditWarehouseProductsView from './EditWarehouseProductsView.vue';
import axios from 'axios';
import store from '@/store'; // import your Vuex store

export default {
  name: 'WarehouseView',
  components: {
    EditWarehouseView,
    EditWarehouseProductsView,
    SaveWarehouseView,
  },
  data() {
    return {
      warehouses: [],
      warehouse_id: null,
      showAddWarehouseModal: false,
      showEditWarehouseModal: false,
      showEditWarehouseModalProducts: false,
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
      console.log("here", this.editingWarehouse);
      this.showEditWarehouseModal = true;
    },
    openEditWarehouseModalProducts(warehouse) {
      this.warehouse_id = warehouse.id; 
      this.showEditWarehouseModalProducts = true;
    },
    closeEditWarehouseModal() {
      this.showEditWarehouseModal = false;
    },
    closeEditWarehouseModalProducts() {
      this.showEditWarehouseModalProducts = false;
    },
    addWarehouse(newWarehouseData) {
      console.log(newWarehouseData);
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


