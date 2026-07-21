import {useState, useEffect} from 'react';

function StoryGame({story, onNewStory}) {
    const [currentNodeId, setCurrentNodeId] = useState(null);
    const [currentNode, setCurrentNode] = useState(null);
    const [options, setOptions] = useState([])
    const [isEnding, setIsEnding] = useState(false)
    const [isWinningEnding, setIsWinningEnding] = useState(false)

    useEffect(() => {
        if (story && story.root_node) {
            const rootNodeId = story.root_node.id
            setCurrentNodeId(rootNodeId)
        }
    }, [story])

    useEffect(() => {
        if (currentNodeId && story && story.all_nodes) {
            const node = story.all_nodes[currentNodeId]

            setCurrentNode(node)
            setIsEnding(node.is_ending)
            setIsWinningEnding(node.is_winning_ending)

            if (node.options && node.options.length > 0) { 
                setOptions(node.options)
            } else {
                setOptions([])
            }
        }
    }, [currentNodeId, story])

    const chooseOption = (optionId) => {
        setCurrentNodeId(optionId)
    }

    const restartStory = () => {
        if (story && story.root_node) {
            setCurrentNodeId(story.root_node.id)
        }
    }

    return <div className="story-game">
        {/* Story Title: */}
        <header className="story-header">
            <h2>{story.title}</h2>
        </header>

        <div className="story-content">
            {currentNode && <div className="story-node">
                <p>{currentNode.content}</p>    
            
                {isEnding ? <div className="story-ending">
                    <h3>{isWinningEnding ? "Victory" : "The Chronicle Ends"}</h3>
                    <p className={isWinningEnding ? "winning-message" : "ending-message"}>
                        {isWinningEnding 
                            ? "You have carved your name into the legends of Runeterra." 
                            : "Your journey through the realms of Runeterra has reached its conclusion."}
                    </p>
                </div> 
                : 
                <div className="story-options">
                    <h3>Choose Your Path</h3>
                    <div className="options-list">
                        {options.map((option, index) => {
                            return <button 
                                    key={index}
                                    onClick={() => chooseOption(option.node_id)}
                                    className="option-btn"
                                    >
                                    {option.text}
                                </button>
                        })}
                    </div>
                </div>
                }
            </div>}

            <div className="story-controls">
                <button onClick={restartStory} className="reset-btn">
                    Rewind the Chronicle
                </button>

                {onNewStory && <button onClick={onNewStory} className="new-story-btn">
                    Forge New Legend
                </button>}
            </div>
        </div>
    </div>
}

export default StoryGame;