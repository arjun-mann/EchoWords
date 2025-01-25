import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [defClick, setDefClick] = useState(true);
  return (
    <>
      <h1 className = "Title">EchoWords</h1>
      <div className="outer-div">
        <div className="original"><input className="box" placeholder="Enter Text"></input></div>
        <div className="translated"><input className="box" placeholder="Translated Text"></input></div>
      </div>
      <button className="translate-btn">Translate</button>
      <div className="lower-modules">
        {/* <button className="analysis-btn" onClick={setDefClick(true)}>Analyze</button>
        <button className="definition-btn" onClick={setDefClick(false)}>Definitions</button> */}
        
        {/* //   defClick ? <div className="lower-box">Analysis</div> : <div className="lower-box">Definitions</div> */}
        
      </div>
    </>
  )
}

export default App
