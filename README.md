# Lore of Legends — Interactive Story Generator

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://lore-of-legends-pi.vercel.app/)
[![Backend API](https://img.shields.io/badge/API-render.com-46a2f1)](https://lore-of-legends.onrender.com)
[![API Docs](https://img.shields.io/badge/docs-swagger-85ea2d)](https://lore-of-legends.onrender.com/docs)
[![Python](https://img.shields.io/badge/python-3.14+-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/react-19-61dafb)](https://react.dev/)

A full-stack interactive story generation platform where users input a theme and navigate **LLM-generated branching narratives** with multiple dynamic endings. Powered by Google Gemini via LangChain, built with FastAPI and React.

## ✨ Features

- **🎭 Theme-Based Generation** — Enter any theme (e.g., pirates, space, medieval fantasy) and get a unique branching story.
- **🌳 Branching Narratives** — Each non-ending node offers 2–3 meaningful choices, creating a tree structure 3–4 levels deep.
- **🏆 Multiple Endings** — Stories include both winning and losing endings across paths of varying lengths.
- **⏳ Async Job Processing** — Long-running LLM inference runs in the background via FastAPI's `BackgroundTasks`; the frontend polls for status in real time.
- **🧠 LLM-Powered** — Uses Google Gemini (via LangChain) with Pydantic-validated structured output to guarantee deterministic, tree-shaped JSON.
- **📱 Responsive Frontend** — Built with React 19, Vite, and React Router for a fast, client-side experience.

## 🌐 Deployments

| Service | URL |
|---------|-----|
| **Frontend** (Vercel) | [https://lore-of-legends-pi.vercel.app/](https://lore-of-legends-pi.vercel.app/) |
| **Backend API** (Render) | [https://lore-of-legends.onrender.com](https://lore-of-legends.onrender.com) |
| **API Docs** (Swagger UI) | [https://lore-of-legends.onrender.com/docs](https://lore-of-legends.onrender.com/docs) |

## 🏗️ Tech Stack

### Backend (`backend/`)

| Technology | Purpose |
|------------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework & REST API |
| [PostgreSQL](https://www.postgresql.org/) | Relational database |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM & database models |
| [LangChain](https://www.langchain.com/) | LLM orchestration framework |
| [LangChain Google GenAI](https://python.langchain.com/docs/integrations/llms/google_genai/) | Google Gemini integration |
| [Pydantic](https://docs.pydantic.dev/) | Data validation & structured output parsing |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |

### Frontend (`frontend/`)

| Technology | Purpose |
|------------|---------|
| [React 19](https://react.dev/) | UI library |
| [Vite](https://vitejs.dev/) | Build tool & dev server |
| [React Router v7](https://reactrouter.com/) | Client-side routing |
| [Axios](https://axios-http.com/) | HTTP client for API calls |

### LLM

- **Google Gemini** (`gemini-2.5-flash-lite`) via LangChain

## 📁 Project Structure

```
lore-of-legends/
├── backend/
│   ├── main.py                    # FastAPI app entry point
│   ├── pyproject.toml             # Python project config & dependencies
│   ├── requirements.txt           # pip dependencies
│   ├── core/
│   │   ├── config.py              # Settings / environment config
│   │   ├── models.py              # Pydantic models for LLM output parsing
│   │   ├── prompts.py             # LLM system prompts
│   │   └── story_generator.py     # Story generation logic (LangChain chain)
│   ├── db/
│   │   └── database.py            # SQLAlchemy engine & session setup
│   ├── models/
│   │   ├── story.py               # Story & StoryNode ORM models
│   │   └── job.py                 # StoryJob ORM model (async processing)
│   ├── routers/
│   │   ├── story.py               # /api/stories/ endpoints
│   │   └── job.py                 # /api/jobs/  endpoints
│   └── schemas/
│       ├── story.py               # Pydantic schemas for story API
│       └── job.py                 # Pydantic schemas for job API
├── frontend/
│   ├── index.html                 # HTML entry point
│   ├── vite.config.js             # Vite configuration
│   ├── package.json               # Node dependencies
│   └── src/
│       ├── main.jsx               # React entry point
│       ├── App.jsx                # Root component with router
│       ├── App.css                # Global styles
│       ├── util.js                # API base URL helper
│       └── components/
│           ├── StoryGenerator.jsx # Theme input & job polling logic
│           ├── StoryLoader.jsx    # Fetches and loads a completed story
│           ├── StoryGame.jsx      # Interactive branching narrative UI
│           ├── ThemeInput.jsx     # Theme submission form
│           └── LoadingStatus.jsx  # Spinner while story generates
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.14+**
- **Node.js 20+** and npm
- **PostgreSQL** instance (local or cloud)
- **Google Gemini API key** (get one from [Google AI Studio](https://aistudio.google.com/))

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jnrgxx/lore-of-legends.git
   cd lore-of-legends/backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS / Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in `backend/`:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/lore_of_legends
   API_KEY=your_gemini_api_key_here
   ALLOWED_ORIGINS=http://localhost:5173
   ```

5. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000` and interactive docs at `http://localhost:8000/docs`.

### Frontend Setup

1. **Navigate to the frontend directory**
   ```bash
   cd lore-of-legends/frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure API URL** (optional)

   Create a `.env` file in `frontend/`:
   ```env
   VITE_API_URL=http://localhost:8000
   ```

4. **Start the dev server**
   ```bash
   npm run dev
   ```

   The app will be available at `http://localhost:5173`.


## ⚙️ API Endpoints

### `POST /api/stories/create`

Create a new story generation job.

**Request body:**
```json
{
  "theme": "pirates"
}
```

**Response (immediate — job queued):**
```json
{
  "job_id": "uuid-string",
  "status": "pending",
  "created_at": "2026-05-07T12:00:00Z"
}
```

### `GET /api/jobs/{job_id}`

Poll for job status.

**Response:**
```json
{
  "job_id": "uuid-string",
  "status": "completed",
  "story_id": 42,
  "created_at": "2026-05-07T12:00:00Z",
  "completed_at": "2026-05-07T12:00:15Z"
}
```

Status values: `pending` → `processing` → `completed` / `failed`

### `GET /api/stories/{story_id}/complete`

Retrieve the full branching story tree.

**Response:**
```json
{
  "id": 42,
  "title": "The Pirate's Curse",
  "session_id": "uuid-string",
  "created_at": "2026-05-07T12:00:15Z",
  "root_node": {
    "id": 1,
    "content": "You wake up on a deserted island...",
    "is_ending": false,
    "is_winning_ending": false,
    "options": [
      { "text": "Explore the jungle", "node_id": 2 },
      { "text": "Build a raft", "node_id": 3 }
    ]
  },
  "all_nodes": { ... }
}
```

## 💡 How It Works

1. **User enters a theme** — The React frontend sends a `POST /api/stories/create` request with the theme.
2. **Job is queued** — The backend creates a `StoryJob` record with status `pending` and returns a `job_id` immediately.
3. **Background processing** — FastAPI's `BackgroundTasks` calls `StoryGenerator.generate_story()` in a separate database session.
4. **LLM invocation** — LangChain sends the theme + structured prompt to Google Gemini, which returns a complete branching story as JSON.
5. **Pydantic validation** — The raw LLM output is parsed and validated against `StoryLLMResponse`, ensuring deterministic structure.
6. **Database persistence** — The story tree is stored as `Story` and `StoryNode` records (with options as JSON), forming a recursive graph.
7. **Frontend polling** — The React app polls `GET /api/jobs/{job_id}` every 5 seconds until status is `completed`.
8. **Story gameplay** — Once complete, the frontend fetches the full story tree via `GET /api/stories/{story_id}/complete` and renders the interactive branching narrative.

## 📄 License

[MIT](LICENSE)