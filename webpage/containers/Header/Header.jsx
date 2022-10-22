import React from 'react'
import { Cta, HeaderSocials } from '../../components'

function Header() {
  return (
    <header>
      <div className='container header__container'>
        <h2 className='text-light'>Hackaton BBVA</h2>
        <h1>BigMinds Team</h1>
        <h3 className='text-primary'>Reto Retargeting</h3>
        <Cta />
        <HeaderSocials/>
        <div className="me">
          <img src='/assets/upload.svg' alt="me"/>
        </div>

        <a href='#contact' className='scroll__down'>Scroll Down</a>
      </div>
    </header>
  )
}

export default Header