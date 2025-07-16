from typing import Any
import httpx

# GitHub REST API v3 base URL for repository endpoints
# Docs: https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28
GITHUB_REPOSITORIES_API = "https://api.github.com"

# Limit the number of repositories fetched
GITHUB_REPOSITORIES_PER_PAGE = 5

# Sort by the last updated repositories
# Valid sort values per GitHub API docs: created, updated, pushed, full_name
GITHUB_SORT_REPOSITORIES_BY = "updated"

async def fetch_user_repositories(username: str) -> list[dict[str, Any]] | None:
    # Construct the API URL to fetch public repositories for a user
    url = f"{GITHUB_REPOSITORIES_API}/users/{username}/repos"
    
    # Define query parameters based on GitHub API reference:
    # https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-a-user
    params = {
        "sort": GITHUB_SORT_REPOSITORIES_BY,
        "per_page": GITHUB_REPOSITORIES_PER_PAGE
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

        if response.status_code != 200:
            return None

        repos = response.json()

        return [
            {
                "name": repo["name"],
                "html_url": repo["html_url"],
                "description": repo["description"],
                "language": repo["language"]
            }
            for repo in repos
        ]

    except Exception as e:
        print(f"[fetch_user_repos] Error fetching {username}: {e}")
        return None
