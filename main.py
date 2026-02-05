from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

API_KEY = "guvi_voice_api_2026"

class RequestData(BaseModel):
    language: Optional[str] = None
    audio_format: Optional[str] = None
    audio_base64: Optional[str] = None

@app.post("/predict")
def predict(
    data: RequestData,
    x_api_key: str = Header(None)
):
    # 🔒 API key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {
        "status": "success",
        "is_ai_generated": False,
        "confidence": 0.5
    }
