<template>
  <div class="min-w-0 w-full">
    <div class="display-1">Porcentaje de usuarios</div>
    <v-card class="justify-center">
      <div v-if="showChart">
        <apexchart
          width="500"
          :series="series"
          :options="chartOptions"
        ></apexchart>
      </div>
    </v-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'RetargetingPieChartPage',
  data() {
    return {
      showChart: false,
      series: [],
      chartOptions: {
        chart: {
          type: 'donut'
        },
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }],
        labels: ['Call Center', 'WhatsApp']
      }
    }
  },
  computed: {
    ...mapState('app', ['usersList', 'percentage'])
  },
  created() {

  },
  mounted() {
    this.showChart = true
    const factor = this.percentage / 100
    const totalUsers = this.usersList.length

    this.series = [
      factor * totalUsers,
      (1 - factor) * totalUsers
    ]
  }
}
</script>

<style scoped>

</style>
