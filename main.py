from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

API_KEY = "123456"

class RequestData(BaseModel):
    message: str
    audio_url: str

@app.post("/predict")
def predict(data: RequestData, authorization: str = Header(None)):
     if not authorization or "123456" not in authorization:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "status": "success",
        "is_ai_generated": False,
        "confidence": 0.5
    }
