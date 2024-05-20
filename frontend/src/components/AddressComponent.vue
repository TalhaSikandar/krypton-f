<template>
  <div>
    <label class="label" for="city">City</label>
    <input class="input" type="text" id="city" v-model="address.city" placeholder="Enter city" />

    <label class="label" for="country">Country</label>
    <input class="input" type="text" id="country" v-model="address.country" placeholder="Enter country" />
  </div>
</template>

<script>
export default {
  props: {
    address: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      addressData: this.address,
    };
  },
  watch: {
    addressData: {
      handler(newVal) {
        this.$emit('update-address', newVal);
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
