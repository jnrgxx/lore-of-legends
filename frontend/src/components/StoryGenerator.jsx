import {useState, useEffect} from "react"
import {useNavigate} from "react-router-dom";
import axios from "axios";
import ThemeInput from "./ThemeInput";
import LoadingStatus from "./LoadingStatus";
import { API_BASE_URL } from "../util.js";

function StoryGenerator() {
    const navigate = useNavigate()
    const [theme, setTheme] = useState("")
    const [jobId, setJobId] = useState(null)
    const [jobStatus, setJobStatus] = useState(null)
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)

    // poll every 5 seconds to check the Job Status
    useEffect(() => {
        let pollInterval;

        if (jobId && jobStatus === "processing") {
            pollInterval = setInterval(() => {
                pollJobStatus(jobId)
            }, 5000)
        }

        return () => {
            if (pollInterval) {
                clearInterval(pollInterval)
            }
        }

    }, [jobId, jobStatus])

    const generateStory = async (theme) => {
        setLoading(true)
        setError(null)
        setTheme(theme)

        try {
            // start generation:
            const response = await axios.post(`${API_BASE_URL}/stories/create`, {theme})
            // get information back:
            const {job_id, status} = response.data
            setJobId(job_id)
            setJobStatus(status)
            
            // start polling immediately
            pollJobStatus(job_id)
        } catch (e) {
            setLoading(false)
            setError(`Failed to generate story: ${e.message}`)
        }
    } 

    // 
    const pollJobStatus = async (id) => {
        try {
            // get the status of the job id:
             const response = await axios.get(`${API_BASE_URL}/jobs/${id}`)
            //  get the values status, story_id, error from response.data:
             const {status, story_id, error: jobError} = response.data
            setJobStatus(status)

            if (status === "completed" && story_id) {
                // if completed: avigate to the story page:
                fetchStory(story_id)
            } else if (status === "failed" || jobError) {
                setError(jobError || "Failed to generate story")
                setLoading(false)
            }

        } catch (e) {
            if (e.response?.status !== 404) {
                setError(`Failed to check story status: ${e.message}`)
                setLoading(false)
            }
        }
    }

    // function when job is finished and ready to load
    const fetchStory = async (id) => {
        try {
            setLoading(false)
            setJobStatus("completed")
            navigate(`/story/${id}`)
        } catch (e) {
            setError(`Failed to load story: ${e.message}`)
            setLoading(false)
        }
    }

    // function to reset states:
    const reset = () => {
        setJobId(null)
        setJobStatus(null)
        setError(null)
        setTheme("")
        setLoading(false)
    }

    // display errors:
    return <div className="story-generator">
                {error && <div className="error-message">
                    <p>{error}</p>
                    <button onClick={reset}>Try Again</button>
                </div>}
            

                {/* allow to enter theme: */}
                {!jobId && !error && !loading && <ThemeInput onSubmit={generateStory} />}

                {loading && <LoadingStatus theme={theme} />}
            </div>
}

export default StoryGenerator;