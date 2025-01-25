import { useState } from 'react'
import './App.css'

function App() {
  const [defClick, setDefClick] = useState(false);
  return (
    <>
      <h1 className = "Title">EchoWords</h1>
      
      <div className="outer-div">
        <div className="original"><textarea className="box" placeholder="Enter Text"></textarea></div>
        <div className="box translated">Translated Text</div>
      </div>
      
      <button className="translate-btn">Translate</button>
      
      <div className="lower-modules">
        <div className="btn-container">
          <button className="second-btn" onClick={()=>setDefClick(false)}>Analyze</button>
          <button className="second-btn" onClick={()=>setDefClick(true)}>Definitions</button> 
        </div>
        
        {defClick ? <div className="lower-box">Analysis</div> : <div className="lower-box">Definitions</div>}
        
      </div>
    </>
  )
}

export default App
