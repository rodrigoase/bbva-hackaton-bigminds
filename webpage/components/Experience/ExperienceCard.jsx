import React from 'react'

function ExperienceCard(props) {

  return (
    <>
      <div className="experience_card">
        <h3>{props.title}</h3>
        <div className="experience__content">
          {props.children}
        </div>
      </div>
    </>
  )
}

export default ExperienceCard