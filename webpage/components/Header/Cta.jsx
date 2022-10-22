import React from 'react'

function Cta() {
  return (
    <div className='cta'>
      <input type="file" id="upload" accept=".csv" onChange={handleOnChange} hidden/>
      <label for="upload" className='btn'>Subir dataset.cv</label>
      <a href='#about' className='btn btn-primary'>Mira el futuro</a>
    </div>
  )
}

export default Cta