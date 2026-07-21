function LoadingStatus({theme}) {
    return <div className="loading-container">
        <h2>Weaving the Hextech Loom</h2>
        <div className="theme-name">{theme}</div>

        <div className="loading-animation">
            <div className="spinner"></div>
        </div>

        <p className="loading-info">
            The Chronicler of Runeterra is forging your legend
        </p>
    </div>
}

export default LoadingStatus;