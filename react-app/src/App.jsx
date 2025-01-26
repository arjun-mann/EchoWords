import { useState } from 'react'
import './App.css'

function App() {
  const [defClick, setDefClick] = useState(false);
  const [msg, setMSG] = useState("");
  let [analysis, setAnalysis] = useState({
    sentence: "",
    translation : "",
    structure :"",
    analysis : "",
  });
  async function getData(){
    console.log("get data started");
    // url = "http://127.0.0.1:5000/wtran"
    // try{
    fetch("http://127.0.0.1:5000/stran", {
      method: "POST",
      headers: {
        "Content-type" : "application/json",
      },
      body: msg,
    })
      .then((res => res.json)
      .then(data => {setAnalysis({
        sentence: data.sentence,
        translation: data.translation,
        structure: data.structure,
        analysis: data.analysis,
      });
    })
  );
  


      
    //   console.log('5');
      // let parsed_sentence = JSON.parse(json_sentence);
      // parsed_sentence.forEach((e) => {
      //   // textEl.textContent += "..."
      //   setAnalysis(analysis += "Sentence: ");
      //   setAnalysis(analysis += e["Sentence"]);
      //   setAnalysis(analysis += "Translation: ");
      //   setAnalysis(analysis += e["Translation"]);
      //   setAnalysis(analysis += "Grammatical Structure: ");
      //   setAnalysis(analysis += e["Grammatical Structure"]);
      //   setAnalysis(analysis+= "Analysis: ")
      //   setAnalysis(analysis+= e["Analysis"])
    //   });


      // console.log(analysis);
      // setMSG("");
    // }
    // catch (error){
    //   console.error(error.message);
    // }
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
