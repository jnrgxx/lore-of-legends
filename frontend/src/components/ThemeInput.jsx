import {useState} from "react"

const EXAMPLE_THEMES = [
  "Piltover", "Zaun", "Demacia", "Noxus", "Freljord",
  "Ionia", "Shurima", "Shadow Isles", "Targon", "Bilgewater"
]

function ThemeInput({onSubmit}) {
    const [theme, setTheme] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
    
        if (!theme.trim()) {
            setError("Every legend needs a realm. Enter a Runeterra region.");
            return
        }

        onSubmit(theme);
    }

    const handleExampleClick = (example) => {
        setTheme(example);
        setError("");
    }

    return <div className="theme-input-container">
        <h2>Choose Your Realm</h2>
        <p>Enter a region of Runeterra to forge your legend within</p>

        <form onSubmit={handleSubmit}>
            <div className="input-group">
                <input
                    type="text"
                    value={theme}
                    onChange={(e) => {setTheme(e.target.value); setError("")}}
                    placeholder="e.g. Piltover, Demacia, Shadow Isles..."
                    className={error ? 'error' : ''}
                />

                {error && <p className="error-text">{error}</p>}
            </div>
            <button type="submit" className="generate-btn">
                Forge Chronicle
            </button>
        </form>

        <div className="examples">
            <h3>Realms of Runeterra</h3>
            <ul>
                {EXAMPLE_THEMES.map((example) => (
                    <li key={example} onClick={() => handleExampleClick(example)}>
                        {example}
                    </li>
                ))}
            </ul>
        </div>
    </div>
}

export default ThemeInput;