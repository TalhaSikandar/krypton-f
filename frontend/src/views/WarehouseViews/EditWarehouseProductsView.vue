<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Warehouse Products</strong></p>
        <button class="delete cross-icon-button" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <div v-if="warehouse.products.length">
          <h2 class="product_heading"><strong>Products:</strong></h2>
          <table class="products-table">
            <thead>
              <tr>
                <th>Product Name</th>
                <th>Quantity</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="product in warehouse.products" :key="product.product.id">
                <td>{{ product.product.product_name }}</td>
                <td>{{ product.available_quantity }}</td>
                <td>
                  <button class="button remove-button" @click="removeProduct(product.product.id)">Remove</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else>
          <p><strong>No products available.</strong></p>
        </div>
        <button class="button is-success" @click="showAddProductCard = true">Add a product</button>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="save">Save Products</button>
        <button class="button close-button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
  <add-product-view
    v-if="showAddProductCard"
    @close="closeAddProductCard"
    @save="closeAddProductCard"
    :warehouseId="warehouse_Id"
  ></add-product-view>
</template>

<script>
import AddProductView from './AddProductView.vue';
import axios from 'axios';
import store from '@/store'; // import your Vuex store
export default {
  components: {
    AddProductView,
  },
  data() {
    return {
      warehouse: {
        products: [],
      },
      showAddProductCard: false,
    };
  },
  props: {
    warehouse_Id: {
      type: Number,
      required: true,
    },
  },
  methods: {
    async fetchWarehouseData() {
      await axios.get(`/dashboard/warehouses/${this.warehouse_Id}/products`, {
        headers: {
          Authorization: `Bearer ${store.state.token}`,
        },
      })
        .then(response => {
          this.warehouse.products = response.data;
        console.log(this.warehouse.products);
        })
        .catch(error => {
          alert(error.response.data.error);
        });
    },
    close() {
      this.$emit('close');
    },
    save() {
      this.$emit('save', this.warehouse);
      this.$emit('close');
    },
    closeAddProductCard() {
      this.showAddProductCard = false;
    },
    removeProduct(productId) {
      this.warehouse.products = this.warehouse.products.filter(product => product.product.id !== productId);
    },
  },
  mounted() {
    this.fetchWarehouseData();
    document.title = 'Products | Krypton';
  },
};
</script>

<style scoped>
.product_heading {
  color: var(--white-background-color) !important;
}
</style>
