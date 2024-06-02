<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Warehouse Products</strong></p>
        <button class="delete cross-icon-button"@click="close"></button>
      </header>
      <section class="modal-card-body">
          <div v-if="warehouse.products.length">
            <p><strong>Products:</strong></p>
            <ul>
              <li v-for="product in warehouse.products" :key="product.product.id">
                {{ product.product.product_name }} - Quantity: {{ product.quantity }}
              </li>
            </ul>
          </div>
        <button class="button is-success" @click="this.showAddProductCard=true">Add a product</button>
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
      :warehouse_id="warehouse_id"
    ></add-product-view>
</template>

<script>
import AddProductView from'./AddProductView.vue';
import axios from 'axios';
import store from '@/store'; // import your Vuex store
export default {
  components: {
    AddProductView,
  },
  data () {
    return {
      warehouse: {
        products: '',
      },
      showAddProductCard: false,
    };
  },
  props: {
    warehouse_id: {
      type: Number,
      required: true
    },
  },
  methods: {
   async fetchWarehouseData() {
      console.log(this.warehouse_id);
     await axios.get(`/dashboard/warehouses/${this.warehouse_id}/products`, {
        headers: {
            Authorization: `Bearer ${store.state.token}`
          },
      })
        .then(response => {
          this.warehouse = response.data;
        }).catch(error => {
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
      showAddProductCard = false; 
    },
  },
  mounted() {
    this.fetchWarehouseData();
    document.title = 'Products | Krypton'
  },
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
