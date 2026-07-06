from pydantic import BaseModel

class AdviceRequest(BaseModel):
    message : str

class AdviceResponse(BaseModel):
    advice : str
    