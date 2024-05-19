<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">{{ formTitle }}</p>
        <button class="delete" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <div v-for="(field, key) in fields" :key="key" class="field">
          <label class="label">{{ field.label }}</label>
          <div class="control">
            <input
              v-model="formData[key]"
              class="input"
              :type="field.type"
              :placeholder="field.placeholder"
            />
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="save">{{ formTitle }}</button>
        <button class="button" @click="close">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    fields: {
      type: Object,
      required: true
    },
    formData: {
      type: Object,
      required: true
    },
    formTitle: {
      type: String,
      required: true
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    save() {
      this.$emit('save', this.formData);
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
<!-- <template> -->
<!--   <div class="modal is-active"> -->
<!--     <div class="modal-background" @click="close"></div> -->
<!--     <div class="modal-card"> -->
<!--       <header class="modal-card-head"> -->
<!--         <p class="modal-card-title">{{ formTitle }}</p> -->
<!--         <button class="delete" @click="close"></button> -->
<!--       </header> -->
<!--       <section class="modal-card-body"> -->
<!--         <div v-for="(field, key) in fields" :key="key" class="field"> -->
<!--           <label class="label">{{ field.label }}</label> -->
<!--           <div class="control"> -->
<!--             <input -->
<!--               v-model="formData[key]" -->
<!--               class="input" -->
<!--               :type="field.type" -->
<!--               :placeholder="field.placeholder" -->
<!--             /> -->
<!--           </div> -->
<!--         </div> -->
<!--       </section> -->
<!--       <footer class="modal-card-foot"> -->
<!--         <button class="button is-success" @click="save">{{ formTitle }}</button> -->
<!--         <button class="button" @click="close">Cancel</button> -->
<!--       </footer> -->
<!--     </div> -->
<!--   </div> -->
<!-- </template> -->
<!---->
<!-- <script> -->
<!-- export default { -->
<!--   props: { -->
<!--     fields: { -->
<!--       type: Object, -->
<!--       required: true -->
<!--     }, -->
<!--     formData: { -->
<!--       type: Object, -->
<!--       required: true -->
<!--     }, -->
<!--     formTitle: { -->
<!--       type: String, -->
<!--       required: true -->
<!--     } -->
<!--   }, -->
<!--   methods: { -->
<!--     close() { -->
<!--       this.$emit('close'); -->
<!--     }, -->
<!--     save() { -->
<!--       this.$emit('save', this.formData); -->
<!--     } -->
<!--   } -->
<!-- }; -->
<!-- </script> -->
<!---->
<!-- <style scoped> -->
<!-- /* Add any custom styles if needed */ -->
<!-- </style> -->
<!---->
