import React, { useState } from 'react'
import { AiOutlineHome, AiOutlineUser } from 'react-icons/ai'
import { BiBook, BiMessageSquareDetail } from 'react-icons/bi'
import { RiServiceLine } from 'react-icons/ri'

function Navbar() {
  const [activeNav, setActiveNav] = useState('#')

  function handleClick(tag){
    setActiveNav(tag)
  }

  return (
    <nav>
      <a href='#' onClick={() => handleClick("#")} className={activeNav==="#"?"active":""}><AiOutlineHome/></a>
      <a href='#about' onClick={() => handleClick("#about")} className={activeNav==="#about"?"active":""}><AiOutlineUser/></a>
      <a href='#experience' onClick={() => handleClick("#experience")} className={activeNav==="#experience"?"active":""}><BiBook/></a>
      <a href='#services' onClick={() => handleClick("#services")} className={activeNav==="#services"?"active":""}><RiServiceLine/></a>
      <a href='#contact' onClick={() => handleClick("#contact")} className={activeNav==="#contact"?"active":""}><BiMessageSquareDetail/></a>
    </nav>
  )
}

export default Navbar