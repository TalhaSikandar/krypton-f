<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Add Store</strong></p>
        <button class="delete" @click="close"></button>
      </header>
      <section class="modal-card-body" style="background-color: var(--white-background-color)">
        <div class="field">
          <ContactNormalComponent :contact="store.contact" @update-contact="updateContact" />
        </div>
        <div class="field">
          <AddressComponent :address="store.address" @update-address="updateAddress" />
        </div>
        <div class="field">
          <label class="label" style="color: var(--text-black-color)">Manager Password</label>
          <div class="control">
            <input
              v-model="store.manager_password"
              class="input"
              type="password"
              placeholder="Enter manager password"
            />
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="save">Add Store</button>
        <button class="button close-button is-danger" @click="close">Cancel</button>
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
      store: {
        contact: {
          contact_no: '',
          website: '',
          email: '',
        },
        address: {
          city: '',
          country: '',
        },
        manager_password: ''
      }
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    save() {
      console.log("sending", this.store)
      this.$emit('save', this.store);
      this.$emit('close');
    },
    updateContact(newContact) {
      this.store.contact = newContact;
    },
    updateAddress(newAddress) {
      this.store.address = newAddress;
    }
  },
};
</script>
