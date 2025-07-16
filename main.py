from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from services.github_user_repositories import fetch_user_repositories
from services.self_updater import hourly_update_loop
from datetime import datetime, timezone
from database import get_user, update_user
from models import UserResponse
import asyncio

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def start_scheduler():
    asyncio.create_task(hourly_update_loop())

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.get("/api/user/{username}", response_model=UserResponse)
async def get_user_repos(username: str) -> UserResponse:
    repos = await fetch_user_repositories(username)
    if repos is None:
        raise HTTPException(status_code=404, detail="GitHub user not found or fetch failed")
    
    now = datetime.now(timezone.utc).isoformat()
    existing_user = get_user(username)
    created_at = existing_user.get("created_at") if existing_user else now

    is_new_user = update_user(username, {
        "created_at": created_at,
        "updated_at": now,
        "repositories": repos
    })

    return {
        "username": username,
        "created_at": created_at,
        "updated_at": now,
        "repositories": repos,
        "is_new_user": is_new_user,
        "total_repositories": len(repos)
    }

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})