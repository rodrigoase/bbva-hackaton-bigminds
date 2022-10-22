import React from 'react'
import { Header, About, Experience, Services, Portfolio, Testimonials, Contact, Footer } from '../containers'
import { Navbar } from '../components'
import { client } from '../lib/client'

function index({experiences_data}) {
  return (
    <>
      
      <Header/>
      <Navbar/>
      <About/>
      <Experience data={experiences_data}/>
      <Services/>
      <Portfolio/>
      <Testimonials/>
      <Contact/>
      <Footer/>
    </>
  )
}

export const getServerSideProps = async () => {
  const query = `*[_type == 'experiences']{title, skills[]}`;
  // const query = '*[_type == "experiences"]';
  const experiences_data = await client.fetch(query);
  
  return {
    props: { experiences_data }
  }
}

export default index