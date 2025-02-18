import { useState } from 'react'
import './styles/globals.css'

function App(): JSX.Element {
  const [isDarkMode, setIsDarkMode] = useState<boolean>(false)

  return (
    <div className={`min-h-screen ${isDarkMode ? 'dark' : ''}`}>
      <div className="bg-background text-foreground">
        <main className="container mx-auto px-4 py-8">
          <h1 className="text-4xl font-bold">Welcome to mini-app-v2</h1>
          <button
            onClick={() => setIsDarkMode(!isDarkMode)}
            className="mt-4 px-4 py-2 bg-primary text-primary-foreground rounded-md"
          >
            Toggle {isDarkMode ? 'Light' : 'Dark'} Mode
          </button>
        </main>
      </div>
    </div>
  )
}

export default App
