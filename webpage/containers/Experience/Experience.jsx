import React, { useEffect, useState } from 'react'
import { BsPatchCheckFill } from 'react-icons/bs'
import { ExperienceCard, Skill } from '../../components'

export default function Experience({ data }) {

  return (
    <section id='experience'>
      {console.log(data)}
      <h5>What Skills I Have</h5>
      <h2>My Experience</h2>

      <div className="container experience__container">
        {data?.map((experience) =>
          <ExperienceCard title={experience.title}>
            {experience.skills.map((skill) =>
              <Skill title={skill.name} level={skill.level} Icon={BsPatchCheckFill} />
            )}
          </ExperienceCard>
        )}
      </div>
    </section>
  )
}