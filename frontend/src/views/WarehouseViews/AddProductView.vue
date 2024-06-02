<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Add Product to Warehouse</strong></p>
        <button class="delete cross-icon-button" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <div class="field">
          <label class="label">Product Name</label>
          <div class="control">
            <input v-model="product.product_name" class="input" type="text" placeholder="Enter product name" />
          </div>
        </div>
        <div v-for="(material, index) in rawMaterials" :key="index" class="field">
          <label class="label">{{ `Raw Material ${index + 1}` }}</label>
          <div class="control">
            <input v-model="material.name" class="input" type="text" :placeholder="`Enter raw material ${index + 1}`" />
            <input v-model="material.quantity" class="input" type="number" :placeholder="`Enter quantity for raw material ${index + 1}`" />
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="addProduct">Add Product</button>
        <button class="button close-button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store'; // import your Vuex store

export default {
  data() {
    return {
      product: {
        product_name: '',
        raw_materials: [],
      },
      rawMaterials: [{ name: '', quantity: 0 }], // Initial raw material field
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    addMaterialField() {
      this.rawMaterials.push({ name: '', quantity: 0 });
    },
    async addProduct() {
      this.product.raw_materials = this.rawMaterials;

      try {
        const response = await axios.post(`/dashboard/warehouses/${this.warehouseId}/products/`, this.product, {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        });
        this.$emit('productAdded', response.data);
        this.$emit('close');
      } catch (error) {
        alert(error.response.data.error);
      }
    },
  },
  props: {
    warehouseId: {
      type: Number,
      required: true,
    },
  },
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
