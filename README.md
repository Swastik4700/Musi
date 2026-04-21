# Playlist Recommender 🎵

An AI-powered playlist curation app built with **Python (FastAPI)** + **Vanilla JS** + **Claude API**.

Pick an occasion and vibe → get an instant curated tracklist.

> Built by [Swastik Ranjan Nanda](https://linkedin.com/in/swastiknanda) as a portfolio project.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vanilla HTML/CSS/JS (no framework) |
| Backend | Python 3.11+, FastAPI, Uvicorn |
| AI | Anthropic Claude API (claude-sonnet) |
| Deploy (frontend) | GitHub Pages |
| Deploy (backend) | Render.com (free tier) |

---

## Project Structure

```
playlist-recommender/
├── frontend/
│   └── index.html          # Single-page app
├── backend/
│   ├── main.py             # FastAPI app
│   ├── requirements.txt    # Python dependencies
│   └── render.yaml         # Render deployment config
└── README.md
```

---

## Local Development

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/playlist-recommender.git
cd playlist-recommender
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Set your API key:
```bash
export ANTHROPIC_API_KEY=your_key_here
```

Run the server:
```bash
uvicorn main:app --reload
# API running at http://localhost:8000
```

### 3. Set up the frontend

In `frontend/index.html`, update the `API_BASE` constant:
```js
const API_BASE = "http://localhost:8000";
```

Open `frontend/index.html` in your browser (or use Live Server in VS Code).

---

## Deployment

### Backend → Render.com

1. Push repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo, set root directory to `backend/`
4. Render auto-detects `render.yaml`
5. Add environment variable: `ANTHROPIC_API_KEY` = your key
6. Deploy — copy the URL (e.g. `https://playlist-recommender-api.onrender.com`)

### Frontend → GitHub Pages

1. In `frontend/index.html`, update `API_BASE` to your Render URL:
   ```js
   const API_BASE = "https://playlist-recommender-api.onrender.com";
   ```
2. Go to your GitHub repo → Settings → Pages
3. Set source to `main` branch, `/frontend` folder
4. Your app is live at `https://YOUR_USERNAME.github.io/playlist-recommender`

---

## API Reference

### `POST /generate`

**Request body:**
```json
{
  "occasion": "birthday party",
  "vibe": "high energy and upbeat",
  "duration": 15
}
```

**Response:**
```json
{
  "name": "Midnight Surge",
  "description": "An explosive mix to keep the energy climbing all night.",
  "tracks": [
    { "title": "Blinding Lights", "artist": "The Weeknd", "duration": "3:20" },
    ...
  ]
}
```

### `GET /health`
Returns `{ "status": "ok" }` — useful for Render health checks.

---

## Skills Demonstrated

- **Python** — FastAPI REST API with Pydantic validation
- **JavaScript** — Vanilla JS SPA with async/await fetch
- **API Integration** — Anthropic Claude API (structured JSON prompting)
- **Cloud Deploy** — Render.com (backend), GitHub Pages (frontend)
- **CI/CD ready** — CORS configured, env vars via secrets

---

## License

MIT
