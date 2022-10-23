<template>
  <div class="min-w-0 w-full">
    <div class="display-1">Predicción de usuarios</div>
    <actions-component :class_table="getClass">
      <template v-slot:description></template>
      <template v-slot:actions>
        <v-btn
          outlined
          dense
          color="primary"
          @click="onEnableFilter"
        >
          <v-icon v-if="filterEnabled" small>mdi-filter-off-outline</v-icon>
          <v-icon v-if="!filterEnabled" small>mdi-filter</v-icon>
          Filtrar
        </v-btn>
      </template>
    </actions-component>

    <v-row dense>
      <div :class="getClass">
        <v-card>
          <v-data-table
            :key="keyTable"
            :items="usersList"
            :headers="headers"
          >

          </v-data-table>
        </v-card>
      </div>
      <div v-if="filterEnabled" class="order-md-last order-first col-md-3 col-12 pl-md-0 mb-2">
        <v-card>
          <v-card-title class="pointer">
            Filtros
          </v-card-title>
          <v-card-text>
            <v-row dense>
              <v-col cols="12">
                <v-text-field
                  v-model="percentageInput"
                  outlined
                  dense
                  label="Porcentaje a destinar a call-center"
                  type="number"
                  min="1"
                  max="100"
                  :error-messages="errors"
                ></v-text-field>
              </v-col>
              <v-col cold="12" class="text-right">
                <v-btn class="primary" @click="onProcess">Procesar</v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </div>
    </v-row>
  </div>
</template>

<script>
import { filterMixin } from '@/mixins/filter_mixin'
import ActionsComponent from '@/components/ActionsComponent'
import { mapMutations, mapState } from 'vuex'

export default {
  name: 'RetargetingPage',
  components:{
    ActionsComponent
  },
  mixins: [filterMixin],
  data() {
    return {
      keyTable: 1,
      percentageInput: 0,
      errors: []
    }
  },
  computed: {
    ...mapState('app', ['usersList', 'percentage']),
    headers() {
      let headers = []

      if (this.usersList.length) {
        const [first] = this.usersList

        headers = Object.keys(first).map((property) => {
          return {
            text: property,
            value: property
          }
        })
      }

      return headers
    }
  },
  methods: {
    ...mapMutations('app', ['setPercentage']),
    onProcess() {
      if (this.percentageInput === 0) {
        this.errors.push('Ingrese un número mayor a 0')
      } else {
        this.errors = []
        this.setPercentage(this.percentageInput)
        this.$router.push({ name: 'retargetingPercentage' })
      }
    }
  }
}
</script>

<style scoped>

</style>
