from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Any
from services.github_user_repositories import fetch_user_repositories
from datetime import datetime, timezone

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/user/{username}")
async def get_user_repos(username: str) -> dict[str, Any]:
    repos = await fetch_user_repositories(username)
    if repos is None:
        raise HTTPException(status_code=404, detail="GitHub user not found or fetch failed")
    
    now = datetime.now(timezone.utc).isoformat()
    is_new_user = True
    
    return {
        "username": username,
        "created_at": now,
        "updated_at": now,
        "repositories": repos,
        "is_new_user": is_new_user,
        "total_repositories": len(repos)
    }
