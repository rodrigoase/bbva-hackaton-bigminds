export const filterMixin = {
  data() {
    return {
      filterEnabled: true
    }
  },
  methods: {
    onEnableFilter() {
      this.filterEnabled = !this.filterEnabled
    }
  },
  computed: {
    getClass() {
      if (this.filterEnabled) {
        return 'col-md-9 col-12 order-md-first order-last'
      } else {
        return 'col-12 order-md-first order-last'
      }
    }
  }
}
