from pydantic import BaseModel, Field
from typing import List, Optional


class SessionModel(BaseModel):
    accessToken: str
    authProvider: str = Field(default="auth0")
    expires: str = Field(default="2025-07-16T14:30:58.019Z")
    # models: str | None
    refreshCookie: str | None
    # user: str | None


class AddSessionIn(SessionModel):
    email: str
    isPlus: bool = False





