<template>
  <div class="row">
    <div class="d-flex" style="flex-wrap: wrap" :class="class_table">
      <div class="col-md-6 col-sm-12 p-0">
        <slot name="description"></slot>
      </div>
      <div
        class="col-md-6 p-0 col-sm-12 text-right"
        style="display: flex;
    justify-content: end;
    align-items: flex-end;"
      >
        <slot name="actions"></slot>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  props: {
    class_table: {
      type: String,
      default: 'col'
    }
  },
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
  }
}
</script>
