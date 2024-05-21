<template>
  <div class="modal is-active">
    <!-- <button class="button is-primary" @click="showEditModal = true">Edit Store</button> -->
    <!-- <div class="modal" :class="{'is-active': showEditModal}"> -->
    <div class="modal-background" @click="close"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Edit Store</p>
          <button class="delete" aria-label="close" @click="close"></button>
        </header>
        <section class="modal-card-body">
          <div class="columns">
            <div class="column is-half">
              <div>
                <label>Manager: </label>
                <span>{{ store.manager }}</span>
              </div>
              <div>
                <label>Store Number: </label>
                <span>{{ store.id }}</span>
              </div>
            </div>
            <div class="column is-half">
              <div v-for="warehouse in warehouses" :key="warehouse.id">
                <h3>{{ warehouse.warehouse_name }}</h3>
                <table class="table is-fullwidth">
                  <thead>
                    <tr>
                      <th>Product Name</th>
                      <th>Quantity</th>
                      <th>Add to Store</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="product in warehouse.products" :key="product.id">
                      <td>{{ product.product_name }}</td>
                      <td>{{ product.quantity }}</td>
                      <td>
                        <input type="number" v-model.number="product.quantityToAdd" min="0">
                        <button @click="addProductToStore(warehouse.id, product.id, product.quantityToAdd)">Add</button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-success" @click="save">Save changes</button>
          <button class="button" @click="close">Cancel</button>
        </footer>
      </div>
    <!-- </div> -->
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store';

export default {
  name: 'EditStoreView',
  props: {
    storeId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      showEditModal: false,
      store: {},
      warehouses: [],
    };
  },
  mounted() {
    // this.fetchStoreData(),
    // this.fetchWarehouses()
  },
  methods: {
   async fetchStoreData() {
      // Fetch store data from the backend
      // console.log("StoreId");
      // console.log(this.storeId);
     await axios.get(`/dashboard/stores/${this.storeId}/`, {
        headers: {
            Authorization: `Bearer ${store.state.token}`
          },
      })
        .then(response => {
          this.store = response.data;
          console.log(this.store.manager.username)
        }).catch(error => {
          alert(error.response.data.error);
        });
    },
   async fetchWarehouses() {
      // Fetch warehouses data from the backend
     await axios.get('/dashboard/warehouses/', {

        headers: {
            Authorization: `Bearer ${store.state.token}`
          },
      })
        .then(response => {
          this.warehouses = response.data.map(warehouse => {
            return {
              ...warehouse,
              products: warehouse.products.map(product => ({
                ...product,
                quantityToAdd: 0
              }))
            };
          });
        }).catch(error => {
          alert(error.response.data.error);
        });
    },
   async addProductToStore(warehouseId, productId, quantity) {
      if (quantity <= 0) {
        alert("Quantity must be greater than 0.");
        return;
      }
     await axios.post(`/dashboard/stores/${this.storeId}/add-product/`, {
        headers: {
          Authorization: `Bearer ${store.state.token}`
        },
        warehouse_id: warehouseId,
        product_id: productId,
        quantity: quantity
      }).then(response => {
          alert(response.data.message);
          this.fetchStoreData(); // Refresh store data
          this.fetchWarehouses(); // Refresh warehouses data
        }).catch(error => {
          alert(error.response.data.error);
        });
    },
  close() {
    this.$emit('close');
  },
  save() {
    this.$emit('save', store);
    this.$emit('close');
  },
  },

  created() {
    this.fetchStoreData();
    this.fetchWarehouses();
  }
};
</script>

<style>
.modal-card {
  max-width: 90%;
  width: auto;
}

.modal-background {
  background-color: rgba(10, 10, 10, 0.86);
}
</style>
