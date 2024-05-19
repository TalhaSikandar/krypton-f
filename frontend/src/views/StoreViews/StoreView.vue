<template>
  <div class="stores">
    <h1>Stores</h1>
    <div class="columns is-multiline">
      <div v-for="store in stores" :key="store.id" class="column is-half">
        <div class="card">
          <div class="card-header">
            <p class="card-header-title">
              {{ store.company.company_name }} - {{ store.id }}
            </p>
            <button class="button is-small" @click="openEditStoreModal(store)">Edit</button>
          </div>
          <div class="card-content">
            <div class="content">
              <p><strong>Manager:</strong> {{ store.manager.username }}</p>
              <p v-if="store.contact"><strong>Contact:</strong> {{ store.contact }}</p>
              <p v-if="store.address"><strong>Address:</strong> {{ store.address }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <button class="button is-primary" @click="openAddStoreModal">Add Store</button>
    <generic-form-component
      v-if="showAddStoreModal"
      @close="closeAddStoreModal"
      @save="addStore"
      :fields="storeFields"
      :form-data="editingStore"
      form-title="Add Store"
    ></generic-form-component>
    <generic-form-component
      v-if="showEditStoreModal"
      @close="closeEditStoreModal"
      @save="saveStore"
      :fields="storeFields"
      :form-data="editingStore"
      form-title="Edit Store"
    ></generic-form-component>
  </div>
</template>

<script>
import GenericFormComponent from './GenericFormComponent.vue';
import axios from 'axios';

export default {
  name: 'StoreView',
  components: {
    GenericFormComponent
  },
  data() {
    return {
      stores: [],
      showAddStoreModal: false,
      showEditStoreModal: false,
      editingStore: null,
      storeFields: {
        // company: { label: 'Company', type: 'text', placeholder: 'Company' },
        // manager: { label: 'Manager', type: 'text', placeholder: 'Manager' },
        contact: { label: 'Contact', type: 'text', placeholder: 'Contact' },
        address: { label: 'Address', type: 'text', placeholder: 'Address' },
        manager_password: { label: 'Manager Password', type: 'password', placeholder: 'Password' } // New password field
      }
    };
  },
  mounted() {
    this.getStores();
  },
  methods: {
    getStores() {
      axios
        .get('dashboard/stores/')
        .then(response => {
          this.stores = response.data;
        })
        .catch(error => {
          console.error('Error fetching stores:', error);
        });
    },
    openAddStoreModal() {
      this.editingStore = { company: '', manager: '', contact: '', address: '', manager_password: '' }; // Include manager_password field
      this.showAddStoreModal = true;
    },
    closeAddStoreModal() {
      this.showAddStoreModal = false;
    },
    openEditStoreModal(store) {
      this.editingStore = { ...store, manager_password: '' }; // Include manager_password field
      this.showEditStoreModal = true;
    },
    closeEditStoreModal() {
      this.showEditStoreModal = false;
    },
    addStore(newStoreData) {
      axios
        .post('dashboard/stores/', newStoreData)
        .then(response => {
          this.stores.push(response.data);
          this.closeAddStoreModal();
        })
        .catch(error => {
          console.error('Error adding store:', error);
        });
    },
    saveStore(updatedStoreData) {
      axios
        .put(`dashboard/stores/${updatedStoreData.id}/`, updatedStoreData)
        .then(response => {
          const index = this.stores.findIndex(store => store.id === response.data.id);
          this.$set(this.stores, index, response.data);
          this.closeEditStoreModal();
        })
        .catch(error => {
          console.error('Error saving store:', error);
        });
    }
  }
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
<!-- <template> -->
<!--   <div class="stores"> -->
<!--     <h1>Stores</h1> -->
<!--     <div class="columns is-multiline"> -->
<!--       <div v-for="store in stores" :key="store.id" class="column is-half"> -->
<!--         <div class="card"> -->
<!--           <div class="card-header"> -->
<!--             <p class="card-header-title"> -->
<!--               {{ store.company.company_name }} - {{ store.id }} -->
<!--             </p> -->
<!--             <button class="button is-small" @click="openEditStoreModal(store)">Edit</button> -->
<!--           </div> -->
<!--           <div class="card-content"> -->
<!--             <div class="content"> -->
<!--               <p><strong>Manager:</strong> {{ store.manager.username }}</p> -->
<!--               <p v-if="store.contact"><strong>Contact:</strong> {{ store.contact }}</p> -->
<!--               <p v-if="store.address"><strong>Address:</strong> {{ store.address }}</p> -->
<!--             </div> -->
<!--           </div> -->
<!--         </div> -->
<!--       </div> -->
<!--     </div> -->
<!---->
<!--     <button class="button is-primary" @click="openAddStoreModal">Add Store</button> -->
<!--     <generic-form-component -->
<!--       v-if="showAddStoreModal" -->
<!--       @close="closeAddStoreModal" -->
<!--       @save="addStore" -->
<!--       :fields="storeFields" -->
<!--       :form-data="editingStore" -->
<!--       form-title="Add Store" -->
<!--     ></generic-form-component> -->
<!--     <generic-form-component -->
<!--       v-if="showEditStoreModal" -->
<!--       @close="closeEditStoreModal" -->
<!--       @save="saveStore" -->
<!--       :fields="storeFields" -->
<!--       :form-data="editingStore" -->
<!--       form-title="Edit Store" -->
<!--     ></generic-form-component> -->
<!--   </div> -->
<!-- </template> -->
<!---->
<!-- <script> -->
<!-- import GenericFormComponent from './GenericFormComponent.vue'; -->
<!-- import axios from 'axios'; -->
<!---->
<!-- export default { -->
<!--   name: 'StoreView', -->
<!--   components: { -->
<!--     GenericFormComponent -->
<!--   }, -->
<!--   data() { -->
<!--     return { -->
<!--       stores: [], -->
<!--       showAddStoreModal: false, -->
<!--       showEditStoreModal: false, -->
<!--       editingStore: null, -->
<!--       storeFields: { -->
<!--         company: { label: 'Company', type: 'text', placeholder: 'Company' }, -->
<!--         manager: { label: 'Manager', type: 'text', placeholder: 'Manager' }, -->
<!--         contact: { label: 'Contact', type: 'text', placeholder: 'Contact' }, -->
<!--         address: { label: 'Address', type: 'text', placeholder: 'Address' } -->
<!--       } -->
<!--     }; -->
<!--   }, -->
<!--   mounted() { -->
<!--     this.getStores(); -->
<!--   }, -->
<!--   methods: { -->
<!--     getStores() { -->
<!--       axios -->
<!--         .get('dashboard/stores/') -->
<!--         .then(response => { -->
<!--           this.stores = response.data; -->
<!--         }) -->
<!--         .catch(error => { -->
<!--           console.error('Error fetching stores:', error); -->
<!--         }); -->
<!--     }, -->
<!--     openAddStoreModal() { -->
<!--       this.editingStore = { company: '', manager: '', contact: '', address: '' }; -->
<!--       this.showAddStoreModal = true; -->
<!--     }, -->
<!--     closeAddStoreModal() { -->
<!--       this.showAddStoreModal = false; -->
<!--     }, -->
<!--     openEditStoreModal(store) { -->
<!--       this.editingStore = { ...store }; -->
<!--       this.showEditStoreModal = true; -->
<!--     }, -->
<!--     closeEditStoreModal() { -->
<!--       this.showEditStoreModal = false; -->
<!--     }, -->
<!--     addStore(newStoreData) { -->
<!--       axios -->
<!--         .post('dashboard/stores/', newStoreData) -->
<!--         .then(response => { -->
<!--           this.stores.push(response.data); -->
<!--           this.closeAddStoreModal(); -->
<!--         }) -->
<!--         .catch(error => { -->
<!--           console.error('Error adding store:', error); -->
<!--         }); -->
<!--     }, -->
<!--     saveStore(updatedStoreData) { -->
<!--       axios -->
<!--         .put(`dashboard/stores/${updatedStoreData.id}/`, updatedStoreData) -->
<!--         .then(response => { -->
<!--           const storeIndex = this.stores.findIndex(s => s.id === updatedStoreData.id); -->
<!--           if (storeIndex !== -1) { -->
<!--             this.stores.splice(storeIndex, 1, response.data); -->
<!--           } -->
<!--           this.closeEditStoreModal(); -->
<!--         }) -->
<!--         .catch(error => { -->
<!--           console.error('Error saving store:', error); -->
<!--         }); -->
<!--     } -->
<!--   } -->
<!-- }; -->
<!-- </script> -->
<!-- <style scoped> -->
<!-- .stores { -->
<!-- /* Add your custom styles for the overall stores section */ -->
<!-- } -->
<!---->
<!-- .card { -->
<!-- /* Style the card elements */ -->
<!-- } -->
<!---->
<!-- .card-header-title { -->
<!-- /* Style the card header title */ -->
<!-- } -->
<!---->
<!-- .content { -->
<!-- /* Style the content area within the card */ -->
<!-- } -->
<!-- </style> -->
<!---->
