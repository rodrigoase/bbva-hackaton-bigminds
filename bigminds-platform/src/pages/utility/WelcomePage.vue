<template>
  <div class="pa-2">
    <h1 class="display-2 font-weight-bold">Sube tu CSV</h1>
    <!-- <h2 class="title mt-4">We are almost there! If you want to get notified when the website goes live, subscribe to our mailing list!</h2> -->
    <div class="mt-8">
      <v-file-input
        v-model="file"
        show-size
        accept=".csv"
        chips
        label="Selecciona el archivo(.csv)"
        :error-messages="errors"
      ></v-file-input>
    </div>
    <v-btn color="primary" @click="onImportCSV">Mira el futuro</v-btn>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import UsersService from '@/services/users_service'

export default {
  name: 'WelcomePage',
  data() {
    return {
      file: null,
      errors: []
    }
  },
  methods: {
    ...mapMutations('app', ['setUsersList']),
    onImportCSV() {
      if (!this.file) {
        this.errors.push('Por favor, importe un archivo.')
      } else {
        this.errors = []
      }
      const reader = new FileReader()

      reader.readAsText(this.file, 'ISO-8859-1')
      reader.onload = () => {
        const csvOutput = reader.result
        const csvRows = csvOutput.split('\r\n')

        console.log(csvRows)
        if (csvRows[csvRows.length - 1] === '') {
          csvRows.pop()
        }
        let header = csvRows.shift()
        const separator = this.getSeparator(header)

        header = header.split(separator)
        const listToUpload = csvRows.map((element) => {
          const values = element.split(separator)
          const obj = header.reduce((object, header, index) => {
            object[header] = values[index]

            return object
          }, {})

          return obj
        })

        UsersService.getUsers({ users: listToUpload }).then((response) => {
          this.setUsersList(response.output)
        })
        this.$router.push({ name: 'retargeting' })
      }
    },
    getSeparator(row) {
      const separators = [',', ';', '|']
      let separator = ''

      for (separator of separators) {
        if (row.indexOf(separator) !== -1) {
          break
        }
      }

      return separator
    }
  }
}
</script>

<style scoped>

</style>
