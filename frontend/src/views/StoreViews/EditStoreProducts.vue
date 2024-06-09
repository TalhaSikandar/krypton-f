<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Store Products</strong></p>
        <button class="delete cross-icon-button" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <div v-if="store.products.length">
          <h2 class="product_heading">Products:</h2>
          <table class="products-table">
            <thead>
              <tr>
                <th>Product Name</th>
                <th>Quantity</th>
                <th>Sold Amount</th>
                <th>Edit</th>
                <th>Remove</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="product in store.products" :key="product.product.id">
                <td>{{ product.product.product_name }}</td>
                <td>{{ product.available_quantity }}</td>
                <td>{{ product.sold_amount }}</td>
                <td>
                  <button class="button edit-button" @click="editProduct(product)">Edit</button>
                </td>
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
        <button class="button is-success" @click="saveProducts">Save Products</button>
        <button class="button is-info" @click="showMarkSoldCard = true">Mark as Sold</button>
        <button class="button close-button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
  <add-product-view
    v-if="showAddProductCard"
    @close="closeAddProductCard"
    @save="closeAddProductCard"
    :storeId="store_Id"
  ></add-product-view>
  <mark-sold-product-view
    v-if="showMarkSoldCard"
    @close="closeMarkSoldCard"
    :store="store"
  ></mark-sold-product-view>
  <edit-product-view
    v-if="showEditProductCard"
    @close="closeEditProductCard"
    @save="saveProductChanges"
    :editedProduct="editedProduct"
  ></edit-product-view>
</template>

<script>
import AddProductView from './AddProductView.vue';
import EditProductView from './EditProductView.vue';
import MarkSoldProductView from './MarkSoldProductView.vue';
import axios from 'axios';
import store from '@/store'; // import your Vuex store
import { Radar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, RadialLinearScale, PointElement, LineElement, Filler } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, RadialLinearScale, PointElement, LineElement, Filler);

export default {
  components: {
    AddProductView,
    MarkSoldProductView,
    EditProductView,
  },
  data() {
    return {
      store: {
        products: [],
      },
      showAddProductCard: false,
      showMarkSoldCard: false,
      showEditProductCard: false,
      editedProduct: '',
    };
  },
  props: {
    store_Id: {
      type: Number,
      required: true,
    },
  },
  methods: {
    async saveProducts() {
      try {
        for (const product of this.store.products) {
          const response = await axios.put(
            `/dashboard/stores/${product.store.id}/products/${product.product.id}/`,
            {
              available_quantity: product.available_quantity,
              sold_amount: 0,
              id: product.id
            },
            {
              headers: {
                authorization: `Bearer ${store.state.token}`,
              }
            }
          );
          // Update the local product data after successful response
          product.available_quantity -= product.sold_amount;
          product.sold_amount = 0; // Reset sold amount
        }
      } catch (error) {
        alert(error.response.data.error || 'Error marking product as sold');
      }
    },
    async fetchStoreData() {
      try {
        const productResponse = await axios.get(`/dashboard/stores/${this.store_Id}/products`, {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        });

        const productData = productResponse.data; // Store product data
        console.log(productData, "hi"); // Log the enriched products array

        // Extract store and product IDs for efficient fetching
        const productIds = productData.map(product => parseInt(product.product, 10));
        const storeIds = productData.map(product => parseInt(product.store, 10));

        // Create a promise array for parallel store fetching
        const storePromises = storeIds.map(storeId => {
          return axios.get(`/dashboard/stores/${storeId}`, {
            headers: {
              Authorization: `Bearer ${store.state.token}`,
            },
          });
        });

        // Wait for all store requests to complete and fetch product details
        const storeResponses = await Promise.all(storePromises);
        console.log(productIds, "all ids")
        const productDetailsPromises = productIds.map(productId => {
          return axios.get(`/dashboard/stores/${productId}/products_r`, { // Assuming a separate endpoint for product details
            headers: {
              Authorization: `Bearer ${store.state.token}`,
            },
          });
        });

        const productDetailsResponses = await Promise.all(productDetailsPromises);

        // Combine product data with fetched stores and product details (efficiently)
        this.products = productData.map((product, index) => {
          return {
            ...product, // Spread product data (including ID)
            store: storeResponses[index].data,
            product: productDetailsResponses[index].data, // Assuming product details response structure
          };
        });
        this.store.products = this.products


        console.log(this.products[0]); // Log the enriched products array
      } catch (error) {
        alert(error.response.data.error || 'Error fetching store and product data'); // Handle errors with a default message
      }
    },
    close() {
      this.$emit('close');
    },
    save() {
      this.$emit('save', this.store);
      this.$emit('close');
    },
    closeAddProductCard() {
      this.showAddProductCard = false;
    },
    closeMarkSoldCard() {
      this.showMarkSoldCard = false;
    },
    removeProduct(productId) {
      this.store.products = this.store.products.filter(product => product.product.id !== productId);
    },
    editProduct(product) {
      // Set the edited product and show the edit product view
      this.editedProduct = { ...product }; // Create a copy to avoid directly modifying the original
      this.showEditProductCard = true;
    },
    closeEditProductCard() {
      // Set the edited product and show the edit product view
      this.showEditProductCard = false;
    },
    saveProductChanges(editedProduct) {
      // Update the original product with edited details
      const index = this.store.products.findIndex(product => product.product.id === editedProduct.product.id);
      if (index !== -1) {
        this.store.products[index].available_quantity = editedProduct.available_quantity;
        // Other fields can also be updated similarly
      }
      this.showEditProductCard = false; // Hide the edit product view after saving
    },
  },
  mounted() {
    this.fetchStoreData();
    document.title = 'Products | Krypton';
  },
};
</script>

<style scoped>
.product_heading {
  color: var(--white-background-color) !important;
}
</style>
