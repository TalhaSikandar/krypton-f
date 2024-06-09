<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Add Products to Store</strong></p>
        <button class="delete cross-icon-button" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <!-- Product Selection and Quantity Input on a Single Row -->
        <div class="field is-grouped">
          <div class="control is-expanded">
            <label class="label product-card" style="color: var(--white-background-color)">Select Product</label>
            <div class="select is-fullwidth">
              <select v-model="selectedProduct" @change="updateSelectedProduct">
                <option v-for="product in products" :key="product.product.id" :value="product">
                  {{ product.product.product_name }} - {{ product.warehouse.warehouse_name }} (Available: {{ product.available_quantity }})
                </option>
              </select>
            </div>
          </div>
          <div class="control">
            <label class="label product-card" style="color: var(--white-background-color)">Quantity</label>
            <input v-model.number="quantity" class="input" type="number" min="1" placeholder="Enter quantity" @input="checkQuantity" />
          </div>
        </div>
        <button class="button is-primary" @click="addTempProduct">Add this</button>
        <!-- Temporary List of Products to be Added -->
        <div class="field">
          <ul>
            <li v-for="(product, index) in tempProducts" :key="index">
              {{ product.product.product_name }} - {{ product.available_quantity }} (Warehouse: {{ product.warehouse_name }})
              <button @click="removeTempProduct(index)" class="button is-small is-danger">Remove</button>
            </li>
          </ul>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="addProductsToStore">Add Products</button>
        <button class="button close-button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store'; // import your Vuex store
import { toast } from 'bulma-toast';

export default {
  data() {
    return {
      products: [], // List of products from warehouses
      selectedProduct: null, // Selected product from dropdown
      quantity: 1, // Quantity to add to the store
      tempProducts: [], // Temporary list of products to be added
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    async fetchWarehouseProducts() {
      try {
        const response = await axios.get('/dashboard/warehouses/products/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        });
        this.products = response.data.map(item => ({
          ...item,
          warehouse: Number(item.warehouse),
        }));
        console.log(this.products, "all products+warehouses");

        const responseWarehouses = await axios.get('/dashboard/warehouses/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        });
        const warehouses = responseWarehouses.data;
        console.log(warehouses, "all warehouses");

        // Match supplier IDs and create a new list accordingly
        const updatedproducts = this.products.map(product => {
          const matchedWarehouse = warehouses.find(warehouse => warehouse.id === product.warehouse);
          return {
            ...product,
            warehouse: matchedWarehouse ? matchedWarehouse : 'Unknown Warehouse',
          };
        });

        this.products = updatedproducts;
        console.log(this.products, "updated products");
      } catch (error) {
        alert(error.response.data.error);
      }
    },
    updateSelectedProduct() {
      this.quantity = 1;
    },
    checkQuantity() {
      if (this.quantity < 1) {
        this.quantity = 1;
      } else if (this.selectedProduct && this.quantity > this.selectedProduct.available_quantity) {
        this.quantity = this.selectedProduct.available_quantity;
        toast({
          message: `The specified amount cannot be added as it exceeds the available quantity.`,
          type: 'is-warning',
          duration: 5000,
        });
      }
    },
    addTempProduct() {
      if (!this.selectedProduct || this.quantity > this.selectedProduct.available_quantity) {
        toast({
          message: `Please select a valid product and quantity.`,
          type: 'is-warning',
          duration: 5000,
        });
        return;
      }
      const tempProduct = {
        product: this.selectedProduct.product,
        warehouse_name: this.selectedProduct.warehouse.warehouse_name,
        warehouse_id: this.selectedProduct.warehouse.id,
        available_quantity: this.quantity,
      };
      this.tempProducts.push(tempProduct);
      this.selectedProduct = null;
      this.quantity = 1;
    },
    removeTempProduct(index) {
      this.tempProducts.splice(index, 1);
    },
    async addProductsToStore() {
      const productData = this.tempProducts.map(product => ({
        product_id: product.product.id,
        warehouse_id: product.warehouse_id,
        available_quantity: product.available_quantity,
      }));

      try {
        const response = await axios.post(`/dashboard/stores/${this.storeId}/products/`, { products: productData }, {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        });
        this.$emit('productsAdded', response.data);
        this.$emit('close');
      } catch (error) {
        alert(error.response.data.error);
      }
    },
  },
  mounted() {
    this.fetchWarehouseProducts();
  },
  props: {
    storeId: {
      type: Number,
      required: true,
    },
  },
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
