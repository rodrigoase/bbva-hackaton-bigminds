import axios from 'axios'

const appApis = axios.create({
  baseURL: 'https://bbva-hackaton-bigminds.de.r.appspot.com'
})

export default {
  getUsers(data = {}) {
    const body = { ...data }

    return appApis.post('', body).then((response) => {
      return response.data
    })
  }
}
