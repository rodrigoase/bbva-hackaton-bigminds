import React from 'react'

function Skill({ title, level, Icon }) {
  return (
    <>
      <article className='experience__details'>
        <Icon className='experience__details-icon' />
        <div>
          <h4>{title}</h4>
          <small className='text-light'>{level}</small>
        </div>
      </article>
    </>
  )
}

export default Skill