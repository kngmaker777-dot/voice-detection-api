from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import os

app = FastAPI()

# HTTP Bearer security
security = HTTPBearer()

# REAL API KEY (recommended: use env variable)
API_KEY = os.getenv("API_KEY", "guvi_voice_api_2026")

class RequestData(BaseModel):
    message: str
    audio_url: str

@app.post("/predict")
def predict(
    data: RequestData,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    # 🔒 API key validation
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return {
        "status": "success",
        "is_ai_generated": False,
        "confidence": 0.5
    }
