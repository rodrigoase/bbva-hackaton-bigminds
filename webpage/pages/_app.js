import '../styles/globals.css'
import '../styles/index.css'
import '../containers/Header/header.css'
import '../containers/About/about.css'
import '../containers/Experience/experience.css'
import '../components/Navbar/navbar.css'

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}

export default MyApp
