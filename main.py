from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

app = FastAPI()

security = HTTPBearer()

class RequestData(BaseModel):
    message: str
    audio_url: str

@app.post("/predict")
def predict(
    data: RequestData,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    return {
        "status": "success",
        "is_ai_generated": False,
        "confidence": 0.5,
        "received_token": credentials.credentials
    }
