<template>
  <div class="dashboard-content-container">
    <h1>Suppliers</h1>
    <div class="columns is-multiline">
      <div v-for="supplier in suppliers" :key="supplier.id" class="column is-4">
        <div class="card">
          <div class="card-header">
            <p class="card-header-title">
              Supplier - {{ supplier.name }}
            </p>
            <button class="button edit-button is-small" @click="openEditSupplierModal(supplier)">Edit</button>
          </div>
          <div class="card-content">
            <div class="content">
              <p v-if="supplier.contact"><strong>Contact:</strong> {{ supplier.contact.email }}</p>
              <p v-if="supplier.address"><strong>Address:</strong> {{ supplier.address.city }} - {{ supplier.address.country }}</p>
            </div>
          </div>
            <button class="button view-raw-materials is-small" @click="openRawMaterialModal(supplier)">View Raw Materials</button>
        </div>
      </div>
    </div>

    <p v-if="!this.suppliers.length">You have got no Suppliers, Kindly Add!</p>
    <button @click="openAddSupplierModal" class="button add-store" style="background-color: var(--primary-color); color: var(--text-color)">Add Supplier</button>

    <save-supplier-view
      v-if="showAddSupplierModal"
      @close="closeAddSupplierModal"
      @save="addSupplier"
      :newSupplier="newSupplierData"
    ></save-supplier-view>

    <edit-supplier-view
      v-if="showEditSupplierModal"
      :supplierId="currentSupplier"
      @close="closeEditSupplierModal"
      @save="saveSupplier"
    ></edit-supplier-view>
    <raw-material-list-view
      v-if="showRawMaterialModal"
      :supplierId="currentSupplier"
      @close="closeRawMaterialModal"
    ></raw-material-list-view>

  </div>
</template>

<script>
import SaveSupplierView from './SaveSupplierView.vue';
import EditSupplierView from './EditSupplierView.vue';
import RawMaterialListView from './RawMaterialListView.vue';
import axios from 'axios';
import store from '@/store'; // import your Vuex store

export default {
  name: 'SupplierView',
  components: {
    SaveSupplierView,
    EditSupplierView,
    RawMaterialListView,
  },
  data() {
    return {
      suppliers: [],
      showAddSupplierModal: false,
      showEditSupplierModal: false,
      showRawMaterialModal: false,
      editingSupplier: null,
      newSupplierData: {
        contact: {
          contact_no: '',
          email: '',
        },
        address: {
          city: '',
          country: '',
        },
      },
      currentSupplier: null,
    };
  },
  mounted() {
    this.getSuppliers();
    document.title = 'Suppliers | Krypton'
  },
  methods: {
    getSuppliers() {
      axios
        .get('dashboard/suppliers/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          this.suppliers = response.data;
          if(this.suppliers)
            console.log("Suppliers", this.suppliers);
        })
        .catch(error => {
          console.error('Error fetching suppliers:', error);
        });
    },
    openAddSupplierModal() {
      this.editingSupplier = { name: '', contact: '', address: '', rawmaterials: [] };
      this.showAddSupplierModal = true;
    },
    closeAddSupplierModal() {
      this.showAddSupplierModal = false;
    },
    openEditSupplierModal(supplier) {
      this.currentSupplier = supplier.id;
      this.editingSupplier = { ...supplier, rawmaterials: supplier.rawmaterials || [] , id: supplier.id};
      this.showEditSupplierModal = true;
    },
    closeEditSupplierModal() {
      this.showEditSupplierModal = false;
    },
    openRawMaterialModal(supplier) {
      console.log(supplier.id,"in sView")
      this.currentSupplier = supplier.id;
      this.showRawMaterialModal = true;
    },
    closeRawMaterialModal() {
      this.showRawMaterialModal = false;
    },
    addSupplier(newSupplierData) {
      console.log(newSupplierData);
      axios
        .post('dashboard/suppliers/', newSupplierData, {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          console.log("here", response.data);
          this.suppliers.push(response.data);
          this.closeAddSupplierModal();
        })
        .catch(error => {
          console.error('Error adding supplier:', error);
        });
    },
    saveSupplier(supplier) {
      console.log(supplier.supplier.rawmaterials, "supplier")
      console.log(supplier.supplierID, "supplierId")
      axios
        .put(`dashboard/suppliers/${supplier.supplierID}/`, supplier.supplier, {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          }
        })
        .then(response => {
          const index = this.suppliers.findIndex(s => s.id === response.data.id);
          console.log(index,"index")
          if (index !== -1) {
            this.suppliers[index] = response.data;
          } else {
            this.suppliers.push(response.data);
          }
          this.closeEditSupplierModal();
        })
        .catch(error => {
          console.error('Error saving supplier:', error);
        });
      console.log("yes")
    }
  }
};
</script>

