from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    message: str
    audio_url: str

@app.post("/predict")
def predict(
    data: RequestData,
    authorization: str = Header(None)
):
    # TEMPORARY relaxed auth (for hackathon testing)
    if authorization is None:
        return {
            "status": "error",
            "message": "Authorization header missing"
        }

    return {
        "status": "success",
        "is_ai_generated": False,
        "confidence": 0.5,
        "received_auth": authorization
    }
