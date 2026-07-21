import './App.css'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import StoryLoader from "./components/StoryLoader"
import StoryGenerator from "./components/StoryGenerator"

function App() {
  return (
    <Router>
      <div className="app-container">
        <header>
          <h1>Lore of <span className="accent">Legends</span></h1>
          <p>Forged in the hextech fires of Runeterra — carve your own legend</p>
        </header>

        <main>
          <Routes>
              <Route path={"/story/:id"} element={<StoryLoader />} />
              <Route path={"/"} element={<StoryGenerator />} />
          </Routes>
        </main>

        <footer>
          <span>A Chronicle of Runeterra — Interactive Story Generator</span>
        </footer>
      </div>
    </Router>
  )
}

export default App