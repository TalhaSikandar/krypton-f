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
          <label class="label product-card" style="color: var(--white-background-color)">Product Name</label>
          <div class="control">
            <input v-model="product.product_name" class="input" type="text" placeholder="Enter product name" />
          </div>
        </div>
        <div class="field">
          <label class="label product-card" style="color: var(--white-background-color)">Unit Weight</label>
          <div class="control">
            <!-- Add unit selector for product -->
            <div class="select">
              <select v-model="product.unit_weight">
                <option value="NORMAL">Normal</option>
                <option value="KG">Kilogram</option>
                <option value="CM">Centimeter</option>
                <option value="LITRE">Litre</option>
              </select>
            </div>
          </div>
        </div>
        <div class="field">
          <label class="label product-card" style="color: var(--white-background-color)">Description</label>
          <div class="control">
            <textarea v-model="product.description" class="textarea" placeholder="Enter description"></textarea>
          </div>
        </div>
        <!-- Raw Materials Table -->
        <table class="table is-bordered is-striped is-narrow is-hoverable">
          <thead>
            <tr>
              <th>Raw Material Name</th>
              <th>Quantity</th>
              <th>Unit Weight</th>
              <th>Unit</th> <!-- Added column for Unit -->
            </tr>
          </thead>
          <tbody>
            <tr v-for="(material, index) in rawMaterials" :key="index">
              <td><input v-model="material.name" class="input" type="text" :placeholder="`Enter raw material ${index + 1} name`" /></td>
              <td><input v-model="material.quantity" class="input" type="number" :placeholder="`Enter quantity for raw material ${index + 1}`" @input="checkQuantity(material)"/></td>
              <td><input v-model="material.unit_weight" class="input" type="text" :placeholder="`Enter unit weight for raw material ${index + 1}`" /></td>
              <td>
                <div class="select">
                  <select v-model="material.unit">
                    <option value="NORMAL">Normal</option>
                    <option value="KG">Kilogram</option>
                    <option value="CM">Centimeter</option>
                    <option value="LITRE">Litre</option>
                  </select>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <button class="button is-info" @click="addMaterialField">Add another raw material</button>
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
        unit_weight: 'NORMAL',
        description: '',
      },
      rawMaterials: [{ name: '', quantity: 1, unit_weight: 'NORMAL' }], // Initial raw material field
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    checkQuantity(material) {
    // Ensure quantity is not below 1
      if (material.quantity < 1) {
      material.quantity = 1; // Set quantity to 1 if below 1
      }
    },
    addMaterialField() {
      this.rawMaterials.push({ name: '', quantity: 1, unit_weight: 'NORMAL' });
    },
    async addProduct() {
      const productData = {
        product_name: this.product.product_name,
        unit_weight: this.product.unit_weight,
        description: this.product.description,
        raw_materials: this.rawMaterials,
      };

      try {
        const response = await axios.post(`/dashboard/warehouses/${this.warehouseId}/products/`, productData, {
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
