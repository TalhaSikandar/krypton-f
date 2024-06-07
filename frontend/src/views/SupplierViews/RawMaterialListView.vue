<template>
  <div class="modal is-active">  <div class="modal-background" @click="close"></div> <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          Raw Materials for Supplier: {{ supplierName }}
        </p>
        <button class="delete" @click="close"></button> </header>
      <div class="card-content">
        <table class="table is-striped">
          <thead>
            <tr>
              <th>Name</th>
              <th>Unit Weight</th>
              <th>Rs/Unit</th>
              <th>Available Quantity</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="rawMaterial in supplierRawMaterials" :key="rawMaterial.id">
              <td>{{ rawMaterial.rawmaterial.rawmaterial_name }}</td>
              <td>{{ rawMaterial.rawmaterial.unit_weight }}</td>
              <td>{{ rawMaterial.rawmaterial.price_per_unit }}</td>
              <td>{{ rawMaterial.available_quantity }}</td>
            </tr>
          </tbody>
        </table>
        <p v-if="!supplierRawMaterials.length">This supplier has no associated raw materials.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store'; // import your Vuex store
export default {
  props: {
    supplierId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      supplierRawMaterials: [],
    };
  },
  mounted() {
    this.fetchRawMaterials();
  },
  methods: {
    close() {
      // Emit an event or perform any necessary actions on closing the card
      this.$emit('close');
    },
    async fetchRawMaterials(supplierId) {
      console.log(this.supplierId, "supplierID")
      try {
        const response = await axios.get(`/dashboard/suppliers/${this.supplierId}/raw_materials/`, {
          headers: {
            Authorization: `Bearer ${store.state.token}`, // Assuming token is stored in store.state
          },
        });
        this.supplierRawMaterials = response.data;
        console.log(this.supplierRawMaterials)
      } catch (error) {
        console.error('Error fetching raw materials:', error);
        // Handle error gracefully (e.g., display an error message to the user)
      }
    }
  },
};
</script>

<style scoped>
.raw-material-list-view {
  /* Add your desired styles here */
}
</style>
