from fastapi import APIRouter
from app.schemas import ChatMessage, ChatRequest, ChatResponse
from app.gemini_client import generate_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_with_bot(data: ChatRequest):
    try:
        history = [
            {"role": msg.role, "parts": msg.parts}
            for msg in data.history
        ]
        reply = generate_response(prompt=data.message, history=data.history)
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}
