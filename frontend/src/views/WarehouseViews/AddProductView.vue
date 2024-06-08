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
              <th>Raw Material - Supplier - Price</th>
              <th>Quantity</th>
              <th>Total Price</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(material, index) in rawMaterials" :key="index">
              <td>
                <div class="select">
                  <select v-model="rawMaterials[index]" @change="updateSupplier(index)">
                    <option v-for="rawmaterial in rawmaterials" :key="rawmaterial.id" :value="rawmaterial">
                      {{ rawmaterial.rawmaterial.rawmaterial_name }} - {{ rawmaterial.supplier.name }} - {{ rawmaterial.rawmaterial.price }}
                    </option>
                  </select>
                </div>
              </td>
              <td>
                <input v-model="material.required_quantity" class="input" type="number" placeholder="Enter quantity" @input="checkQuantity(index)" />
              </td>
              <td>{{ material.rawmaterial.price * material.required_quantity }}</td>
            </tr>
          </tbody>
        </table>
        <button class="button is-info" @click="addMaterialField">Add another raw material</button>
        <!-- Total Cost -->
        <div class="field is-horizontal">
          <div class="field-body" style="display: flex; gap: 20px;">
            <div class="field">
              <label class="label product-card" style="color: var(--white-background-color)">Total Cost/Product</label>
              <div class="control">
                <input class="input" type="text" :value="totalCost" readonly />
              </div>
            </div>
            <div class="field">
              <label class="label product-card" style="color: var(--white-background-color)">Quantity of Product</label>
              <div class="control">
                <input v-model="product.available_quantity" class="input" type="number" placeholder="Enter quantity" @input="checkProductQuantity" />
              </div>
            </div>
            <div class="field">
              <label class="label product-card" style="color: var(--white-background-color)">Total Product Cost</label>
              <div class="control">
                <input class="input" type="text" :value="totalProductCost" readonly />
              </div>
            </div>
          </div>
        </div>
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
import { toast } from 'bulma-toast';

export default {
  data() {
    return {
      product: {
        product_name: '',
        unit_weight: 'NORMAL',
        description: '',
        available_quantity: 1,
      },
      rawmaterials: [], // List of raw material IDs
      rawMaterials: [], // This will hold the full raw material objects
    };
  },
  computed: {
    totalCost() {
      return this.rawMaterials.reduce((total, material) => {
        return total + (material.rawmaterial.price * material.required_quantity);
      }, 0);
    },
    totalProductCost() {
      return this.totalCost * this.product.available_quantity;
    },
  },
  methods: {
    close() {
      this.$emit('close');
    },
    addMaterialField() {
      this.rawMaterials.push({ rawmaterial: {}, supplier: {}, required_quantity: 1 });
    },
    async fetchRawMaterials() {
      try {
        const responseRawMaterials = await axios.get('/dashboard/warehouses/rawmaterials/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        });
        this.rawmaterials = responseRawMaterials.data;

        const responseSuppliers = await axios.get('/dashboard/suppliers/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        });
        const suppliers = responseSuppliers.data;

        // Match supplier IDs and create a new list accordingly
        const updatedRawMaterials = this.rawmaterials.map(rawMaterial => {
          const matchedSupplier = suppliers.find(supplier => supplier.id === rawMaterial.supplier);
          return {
            ...rawMaterial,
            supplier: matchedSupplier ? matchedSupplier : 'Unknown Supplier',
          };
        });

        this.rawmaterials = updatedRawMaterials;
      } catch (error) {
        alert(error.response.data.error);
      }
    },
    async addProduct() {
      const productData = {
        product_name: this.product.product_name,
        unit_weight: this.product.unit_weight,
        description: this.product.description,
        available_quantity: this.product.available_quantity,
        raw_materials: this.rawMaterials.map(material => ({
          rawmaterial: material.rawmaterial,
          required_quantity: material.required_quantity,
        })),
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
    updateSupplier(index) {
    },
    checkQuantity(index) {
      if (this.rawMaterials[index].required_quantity < 1) {
        this.rawMaterials[index].required_quantity = 1;
      }
    },
    checkProductQuantity() {
      for (const material of this.rawMaterials) {
        if (material.required_quantity > material.rawmaterial.available_quantity) {
          toast({
            message: `The specified amount cannot be added as the raw material "${material.rawmaterial.rawmaterial_name}" is low. Kindly contact the supplier or decrease the product quantity.`,
            type: 'is-warning',
            duration: 5000,
          });
          return;
        }
      }
    },
  },
  mounted() {
    this.fetchRawMaterials();
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
