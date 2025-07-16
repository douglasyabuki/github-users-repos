from pydantic import BaseModel
from typing import Optional, List

class Repository(BaseModel):
    name: str
    html_url: str
    description: Optional[str]
    language: Optional[str]

class UserResponse(BaseModel):
    username: str
    created_at: str
    updated_at: str
    repositories: List[Repository]
    is_new_user: bool
    total_repositories: int