from pydantic import BaseModel
from typing import Optional, List

class Repository(BaseModel):
    name: str
    html_url: str
    description: Optional[str] = None
    language: Optional[str] = None


class StoredUser(BaseModel):
    created_at: str
    updated_at: str
    repositories: List[Repository]

class UserResponse(StoredUser):
    username: str
    is_new_user: bool
    total_repositories: int