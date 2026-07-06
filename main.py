from fastapi import FastAPI
from groq_client import get_motivation
from schemas import AdviceRequest



app = FastAPI()

@app.post("/chat")
def chat(Request : AdviceRequest):
    message = Request.message
    response = get_motivation(message)
    return {"reply" : response}