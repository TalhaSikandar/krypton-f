<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Edit Warehouse</strong></p>
        <button class="delete cross-icon-button"@click="close"></button>
      </header>
      <section class="modal-card-body warehouse-mcb">
        <div class="field">
          <label class="label">Warehouse Name</label>
          <div class="control">
            <input
              v-model="formData.warehouse_name"
              class="input"
              type="text"
              placeholder="formData"
            />
          </div>
        </div>
        <div class="field">
          <ContactNormalComponent :contact="warehouse.contact" @update-contact="updateContact" />
        </div>
        <div class="field">
          <AddressComponent :address="warehouse.address" @update-address="updateAddress" />
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="save">Save Warehouse</button>
        <button class="button close-button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
import ContactNormalComponent from '../../components/ContactNormalComponent.vue';
import AddressComponent from '../../components/AddressComponent.vue';

export default {
  components: {
    ContactNormalComponent,
    AddressComponent,
  },
  data() {
    return {
      warehouse: {
        contact: {
          contact_no: '',
          website: '',
          email: '',
        },
        address: {
          city: '',
          country: '',
        },
        warehouse_name: ''
      }
    }
  },
  props: {
    formData: {
      type: Object,
      required: true
    },
  },
  methods: {
    close() {
      this.$emit('close');
    },
    save() {
      this.$emit('save', this.warehouse);
      this.$emit('close');
    },
    updateContact(newContact) {
      this.warehouse.contact = newContact;
    },
    updateAddress(newAddress) {
      this.warehouse.address = newAddress;
    }
  }
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
