from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str  # "user" or "model"
    parts: list

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    reply: str

