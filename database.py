import json
from pathlib import Path
from typing import Any

USERS_FILE = Path("users.json")

def load_users() -> dict[str, Any]:
    if USERS_FILE.exists():
        with USERS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_users(data: dict[str, Any]) -> None:
    with USERS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_user(username: str) -> dict[str, Any] | None:
    users = load_users()
    return users.get(username)

def update_user(username: str, record: dict[str, Any]) -> bool:
    users = load_users()
    is_new_user = username not in users
    users[username] = record
    save_users(users)
    return is_new_user
