<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Edit Store</strong></p>
        <button class="delete" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <!-- Manager and Store ID Section -->
        <div class="columns">
            <div>
              <label>Manager: </label>
              <span v-if="store.manager">{{ store.manager.username }}</span>
              <span v-else>Loading...</span>
            </div>
            <div>
              <label>Store Number: </label>
              <span>{{ store.id }}</span>
            </div>
        </div>

        <div class="field" v-if="store.contact">
          <label class="label">Contact</label>
          <ContactNormalComponent :contact="store.contact" @update-contact="updateContact" />
        </div>
        <div class="field" v-if="store.address">
          <label class="label">Address</label>
          <AddressComponent :address="store.address" @update-address="updateAddress" />
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="save">Save changes</button>
        <button class="button close-button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store';
import ContactNormalComponent from '../../components/ContactNormalComponent.vue';
import AddressComponent from '../../components/AddressComponent.vue';

export default {
  name: 'EditStoreView',
  props: {
    storeId: {
      type: Number,
      required: true
    }
  },
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
        manager: {
          username: ''
        },
      },
    };
  },
  methods: {
    async fetchStoreData() {
      await axios.get(`/dashboard/stores/${this.storeId}/`, {
        headers: {
          Authorization: `Bearer ${store.state.token}`
        },
      })
        .then(response => {
          this.store = response.data;
        }).catch(error => {
          alert(error.response.data.error);
        });
    },
    close() {
      this.$emit('close');
    },
    async save() {
      await axios.put(`/dashboard/stores/${this.storeId}/`, this.store, {
        headers: {
          Authorization: `Bearer ${store.state.token}`
        },
      })
        .then(response => {
          this.$emit('save', response.data);
          this.close();
        }).catch(error => {
          alert(error.response.data.error);
        });
    },
    updateContact(newContact) {
      this.store.contact = newContact;
    },
    updateAddress(newAddress) {
      this.store.address = newAddress;
    },
  },
  created() {
    this.fetchStoreData();
  }
};
</script>

<style scoped>
.modal-card {
  max-width: 90%;
  width: auto;
}

.modal-background {
  background-color: rgba(10, 10, 10, 0.86);
}
</style>
