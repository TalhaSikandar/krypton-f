<template>
  <div>Home</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'landinghome',
  data() {
    return {
      stores: [],
    };
  },
  mounted() {
    document.title = 'Home | Krypton'
  },
  methods: {
  },
};
</script>

<style scoped>
.stores {
  /* Add your custom styles for the overall stores section */
}

.card {
  /* Style the card elements */
}

.card-header-title {
  /* Style the card header title */
}

.content {
  /* Style the content area within the card */
}
</style>

