from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Live ChatBot API",
    version="1.0.0"
)
app.include_router(router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "OK"}
