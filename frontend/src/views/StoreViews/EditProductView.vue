<template>
  <div v-if="editedProduct" class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Edit Product</strong></p>
        <button class="delete cross-icon-button" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <div class="field">
          <label class="label">Product Name</label>
          <input class="input" type="text" v-model="editedProduct.product.product_name" disabled>
        </div>
        <div class="field">
          <label class="label">Available Quantity</label>
          <input class="input" type="number" v-model.number="editedProduct.available_quantity" min="0">
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="saveChanges">Save</button>
        <button class="button close-button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    editedProduct: {
      type: Object,
      required: true,
    },
  },
  methods: {
    close() {
      this.$emit('close');
    },
    saveChanges() {
      // Emit an event to save the edited product details
      this.$emit('save', this.editedProduct);
      this.close(); // Close the edit product view
    },
  },
};
</script>

<style scoped>
/* Add any custom styles as needed */
</style>
