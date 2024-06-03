<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Edit Supplier</strong></p>
        <button class="delete" @click="close"></button>
      </header>
      <section class="modal-card-body" style="background-color: var(--white-background-color)">
        <div class="field">
          <label class="label" style="color: var(--text-black-color)">Name</label>
          <div class="control">
            <input v-model="supplier.name" class="input" type="text" placeholder="Enter supplier name"/>
          </div>
        </div>
        <div class="field">
          <ContactNormalComponent :contact="supplier.contact" @update-contact="updateContact" />
        </div>
        <div class="field">
          <AddressComponent :address="supplier.address" @update-address="updateAddress" />
        </div>
        <div class="field">
          <label class="label" style="color: var(--text-black-color)">Industry</label>
          <div class="control">
            <input
              v-model="supplier.industry"
              class="input"
              type="text"
              placeholder="Enter industry type"
            />
          </div>
        </div>
        <div class="field">
          <label class="label" style="color: var(--text-black-color)">Description</label>
          <div class="control">
            <textarea
              v-model="supplier.description"
              class="textarea"
              placeholder="Enter description"
            ></textarea>
          </div>
        </div>
        <!-- Raw Materials Table -->
        <table class="table is-bordered is-striped is-narrow is-hoverable">
          <thead>
            <tr>
              <th>Raw Material Name</th>
              <th>Quantity</th>
              <th>Unit Weight</th>
              <th>Unit</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(rawmaterial, index) in supplier.rawmaterials" :key="index">
              <td><input v-model="rawmaterial.rawmaterial_name" class="input" type="text" placeholder="Enter raw material ID" /></td>
              <td><input v-model="rawmaterial.available_quantity" class="input" type="number" placeholder="Enter quantity" /></td>
              <td><input v-model="rawmaterial.unit_weight" class="input" type="text" placeholder="Enter unit weight" /></td>
              <td>
                <div class="select">
                  <select v-model="rawmaterial.unit">
                    <option value="NORMAL">Normal</option>
                    <option value="KG">Kilogram</option>
                    <option value="CM">Centimeter</option>
                    <option value="LITRE">Litre</option>
                  </select>
                </div>
              </td>
              <td><button class="button is-danger is-small" @click="removeRawmaterial(index)">Remove</button></td>
            </tr>
          </tbody>
        </table>
        <button class="button is-info" @click="addRawmaterial">Add Raw Material</button>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="update">Update Supplier</button>
        <button class="button close-button is-danger" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
import ContactNormalComponent from '../../components/ContactNormalComponent.vue';
import AddressComponent from '../../components/AddressComponent.vue';
import axios from 'axios';

export default {
  props: {
    supplierId: {
      type: Number,
      required: true,
    },
  },
  components: {
    ContactNormalComponent,
    AddressComponent,
  },
  data() {
    return {
      supplier: {
        name: '',
        contact: {
          contact_no: '',
          email: '',
        },
        address: {
          city: '',
          country: '',
        },
        industry: '',
        description: '',
        rawmaterials: [
          { rawmaterial_id: '', available_quantity: 0, unit_weight: '', unit: 'NORMAL' }
        ]
      }
    };
  },
  created() {
    this.fetchSupplier();
  },
  methods: {
    async fetchSupplier() {
      try {
        const response = await axios.get(`/api/suppliers/${this.supplierId}/`, {
          headers: {
            Authorization: `Bearer ${this.$store.state.token}`,
          },
        });
        this.supplier = response.data;
      } catch (error) {
        console.error('Failed to fetch supplier', error);
      }
    },
    close() {
      this.$emit('close');
    },
    update() {
      this.$emit('update', this.supplier);
    },
    updateContact(contact) {
      this.supplier.contact = contact;
    },
    updateAddress(address) {
      this.supplier.address = address;
    },
    addRawmaterial() {
      this.supplier.rawmaterials.push({ rawmaterial_id: '', available_quantity: 0, unit_weight: '', unit: 'NORMAL' });
    },
    removeRawmaterial(index) {
      this.supplier.rawmaterials.splice(index, 1);
    }
  }
};
</script>
