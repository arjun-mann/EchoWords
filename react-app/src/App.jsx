import { useState } from 'react'
import './App.css'

function App() {
  const [defClick, setDefClick] = useState(false);
  const [msg, setMSG] = useState("");
  async function getData(){
    url = "http://127.0.0.1:5000/wtran"
    try{
      const word_response = new Request("http://127.0.0.1:5000/wtran", {
        method: "POST",
        body: msg,
      })
      const sentence_response = new Request("http://127.0.0.1:5000/stran", {
        method: "POST",
        body: msg,
      })
      const response1 = await fetch(word_response);
      if(!response1.ok)
      {
        throw new Error(`Response status: ${response1.status}`);
      }

      const response2 = await fetch(sentence_response);
      if(!response2.ok)
      {
        throw new Error(`Response status: ${response2.status}`);
      }
      const json = await response.json();

      let parsed = JSON.parse(json_data);
      parse.forEach((e) => {
        textEl.textContent += "..."
        e["Sentence"]
      });


      console.log(json);
      setMSG("");
    }
    catch (error){
      console.error(error.message);
    }
  }
  return (
    <>
      <h1 className = "Title">EchoWords</h1>
      
      <div className="outer-div">
        <div className="original"><textarea className="box" placeholder="Enter Text" onChange={(e) => setMSG(e.target.value)}></textarea></div>
        <div className="box translated">Translated Text</div>
      </div>
      
      <button className="translate-btn" onClick={()=>getData()}>Translate</button>
      
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

export default App;
