from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import anthropic
import json
import os

app = FastAPI(title="Playlist Recommender API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to your GitHub Pages URL in production
    allow_methods=["POST"],
    allow_headers=["*"],
)

from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


class PlaylistRequest(BaseModel):
    occasion: str
    vibe: str
    duration: int  # number of songs


class Track(BaseModel):
    title: str
    artist: str
    duration: str


class PlaylistResponse(BaseModel):
    name: str
    description: str
    tracks: list[Track]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate", response_model=PlaylistResponse)
def generate_playlist(req: PlaylistRequest):
    if req.duration not in [10, 15, 20]:
        raise HTTPException(status_code=400, detail="Duration must be 10, 15, or 20 songs.")

    prompt = f"""You are a music curator. Create a playlist of exactly {req.duration} songs for a {req.occasion} with a {req.vibe} vibe.

Respond ONLY with a valid JSON object. No markdown, no backticks, no preamble.
Format:
{{
  "name": "Creative playlist name",
  "description": "One sentence vibe description (max 12 words)",
  "tracks": [
    {{"title": "Song Title", "artist": "Artist Name", "duration": "3:45"}},
    ...
  ]
}}

Make the songs feel genuinely curated — a mix of iconic and slightly unexpected picks that match the vibe perfectly. All durations should be realistic (between 2:30 and 5:30)."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    clean = raw.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(clean)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse playlist from model.")

    return PlaylistResponse(**data)
