import json
from pathlib import Path
from typing import Optional, Dict
from models import StoredUser

USERS_FILE = Path("users.json")

def load_users() -> dict[str, StoredUser]:
    if USERS_FILE.exists():
        with USERS_FILE.open("r", encoding="utf-8") as f:
            raw = json.load(f)
            return {
                username: StoredUser(**record)
                for username, record in raw.items()
            }
    return {}

def save_users(data: dict[str, StoredUser]) -> None:
    with USERS_FILE.open("w", encoding="utf-8") as f:
        json.dump(
            {username: user.model_dump() for username, user in data.items()},
            f,
            indent=2,
        )

def get_user(username: str) -> Optional[StoredUser]:
    users = load_users()
    return users.get(username)

def update_user(username: str, record: StoredUser) -> bool:
    users = load_users()
    is_new_user = username not in users
    users[username] = record
    save_users(users)
    return is_new_user