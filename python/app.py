"""FastAPI wrapper that serves a Shoelace demo mirroring the Delphi form behavior.

Run locally with:

    uvicorn app:app --reload --port 8000

Then open http://localhost:8000/ to interact with the UI.
"""
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(title="TMS Web Core Shoelace (Python Port)")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Serve the primary page that recreates the Delphi UI using Shoelace components."""
    return TEMPLATES.TemplateResponse("index.html", {"request": request})


@app.get("/health", response_class=HTMLResponse)
async def health() -> str:
    """Lightweight health endpoint useful for containers and uptime checks."""
    return "ok"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
