from pydantic import BaseModel

class InputModel(BaseModel):
    intent: str
    texts: list
    isquestion: bool



    