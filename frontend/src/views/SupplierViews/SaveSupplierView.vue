<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><strong>Add Supplier</strong></p>
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
          <ContactComponent :contact="supplier.contact" @update-contact="updateContact" />
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
              <th>Unit</th>
              <th>Rs/Unit</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(rawmaterial, index) in supplier.rawmaterials" :key="index">
              <td><input v-model="rawmaterial.rawmaterial_name" class="input" type="text" placeholder="Enter raw material ID" /></td>
              <td><input v-model="rawmaterial.available_quantity" class="input" type="number" placeholder="Enter quantity" /></td>
              <td>
                <div class="select">
                  <select v-model="rawmaterial.unit_weight">
                    <option value="NORMAL">Normal</option>
                    <option value="KG">Kilogram</option>
                    <option value="CM">Centimeter</option>
                    <option value="LITRE">Litre</option>
                  </select>
                </div>
              </td>
              <td><input v-model="rawmaterial.price_per_unit" class="input" type="number" placeholder="Enter raw material price" /></td>
              <td><button class="button is-danger is-small" @click="removeRawmaterial(index)">Remove</button></td>
            </tr>
          </tbody>
        </table>
        <button class="button is-info" @click="addRawmaterial">Add Raw Material</button>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="save">Add Supplier</button>
        <button class="button close-button is-danger" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
import ContactComponent from '../../components/ContactComponent.vue';
import AddressComponent from '../../components/AddressComponent.vue';

export default {
  components: {
    ContactComponent,
    AddressComponent,
  },
  data() {
    return {
      supplier: {
        name: '',
        contact: {
          contact_no: '',
          website:'',
          email: '',
        },
        address: {
          city: '',
          country: '',
        },
        industry: '',
        description: '',
        rawmaterials: [
          { rawmaterial_name: '', available_quantity: 0, unit_weight: '',  price_per_unit: '',is_deleted: false, rawmaterial_id:''}
        ]
      }
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    save() {
      // Create a new array to hold formatted raw materials
      const formattedRawmaterials = this.supplier.rawmaterials.map(item => ({
        rawmaterial: {
          rawmaterial_name: item.rawmaterial_name,
          unit_weight: item.unit_weight,
          available_quantity: item.available_quantity,
        },
      }));

      // Update the supplier object with the formatted raw materials
      this.supplier.rawmaterials = formattedRawmaterials;
      console.log(this.supplier.rawmaterials)

      // Emit the 'save' event with the updated supplier data
      this.$emit('save', this.supplier);
    },
    updateContact(contact) {
      this.supplier.contact = contact;
    },
    updateAddress(address) {
      this.supplier.address = address;
    },
    addRawmaterial() {
      this.supplier.rawmaterials.push(
          { rawmaterial_name: '', available_quantity: 0, unit_weight: '',  price_per_unit: '',is_deleted: false, rawmaterial_id:''}
      );
    },
    removeRawmaterial(index) {
      this.supplier.rawmaterials.splice(index, 1);
    }
  }
};
</script>
