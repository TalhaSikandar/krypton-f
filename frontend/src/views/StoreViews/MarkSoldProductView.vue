<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>mark products as sold</strong></p>
        <button class="delete cross-icon-button" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <div v-if="store.products.length">
          <h2 class="product_heading">products:</h2>
          <table class="products-table">
            <thead>
              <tr>
                <th>product name</th>
                <th>available quantity</th>
                <th>sold amount</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="product in store.products" :key="product.product.id">
                <td>{{ product.product.product_name }}</td>
                <td>{{ product.available_quantity }}</td>
                <td>
                  <input v-model="product.sold_amount" type="number" min="0" :max="product.available_quantity">
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else>
          <p><strong>no products available.</strong></p>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="markassold(product)">mark as sold</button>
        <button class="button close-button" @click="close">close</button>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store'; // import your vuex store

export default {
  props: {
    store,
  },
  data() {
  },
  methods: {
    close() {
      this.$emit('close');
    },
    async markassold() {
      try {
        for (const product of this.store.products) {
          if(product.available_quantity - product.sold_amount < 0)
            alert('not enough products to be sold');
          const response = await axios.put(
            `/dashboard/stores/${product.store.id}/products/${product.product.id}/`,
            {
              available_quantity: product.available_quantity - product.sold_amount,
              sold_amount: product.sold_amount,
              id: product.id
            },
            {
              headers: {
                authorization: `bearer ${store.state.token}`,
              }
            }
          );
          // update the local product data after successful response
          product.available_quantity -= product.sold_amount;
          product.sold_amount = 0; // reset sold amount
        }
      } catch (error) {
        alert(error.response.data.error || 'error marking product as sold');
      }
    },
  },
};
</script>

<style scoped>
.product_heading {
  color: var(--white-background-color) !important;
}
</style>
