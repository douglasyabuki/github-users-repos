from datetime import datetime, timezone
import asyncio
from database import load_users, update_user
from services.github_user_repositories import fetch_user_repositories

GITHUB_REQUEST_LIMIT_PER_HOUR = 60
MAX_UPDATES_PER_RUN = 55
GUIDANCE_THRESHOLD = 100  # Suggest using a GitHub token if we hit this

# Delay ensures we stay within GitHub's rate limit
REQUEST_DELAY_SECONDS = 3600 / GITHUB_REQUEST_LIMIT_PER_HOUR  # 60 requests/hour = 1 per 60s
EFFECTIVE_DELAY = max(1.0, REQUEST_DELAY_SECONDS)  # Safety floor: 1s min delay

async def hourly_update_loop():
    while True:
        print("[scheduler] Checking for outdated users...")
        await update_outdated_users()
        print("[scheduler] Sleeping for 1 hour...")
        await asyncio.sleep(3600)

async def update_outdated_users():
    users_data = load_users()
    now = datetime.now(timezone.utc)
    today = now.date()

    outdated = []
    for username, data in users_data.items():
        updated_at_str = data.get("updated_at")
        try:
            updated_at = datetime.fromisoformat(updated_at_str)
            if updated_at.date() < today:
                outdated.append((username, updated_at))
        except Exception:
            outdated.append((username, datetime.min.replace(tzinfo=timezone.utc)))

    if len(outdated) >= GUIDANCE_THRESHOLD:
        print(
            f"[guidance] {len(outdated)} users need updates. "
            "Consider using a GitHub token to increase the rate limit to 5000 requests/hour.\n"
            "See: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/"
            "creating-a-personal-access-token"
        )

    outdated.sort(key=lambda x: x[1])
    users_to_update = outdated[:MAX_UPDATES_PER_RUN]

    for username, _ in users_to_update:
        print(f"[updater] Updating {username}")
        await fetch_and_update_user(username)
        await asyncio.sleep(EFFECTIVE_DELAY)

async def fetch_and_update_user(username: str):
    now = datetime.now(timezone.utc).isoformat()
    repos = await fetch_user_repositories(username)

    if repos is None:
        print(f"[updater] Failed to fetch {username}")
        return

    created_at = load_users().get(username, {}).get("created_at", now)
    update_user(username, {
        "created_at": created_at,
        "updated_at": now,
        "repositories": repos
    })

    print(f"[updater] Updated {username}")
