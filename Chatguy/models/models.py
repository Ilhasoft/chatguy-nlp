from pydantic import BaseModel

class InputSentences(BaseModel):
    intent: str
    texts: list
    isquestion: bool

class InputWords(BaseModel):
    texts: list

class InputCorrections(BaseModel):
    texts: list

class Recover(BaseModel):
    token: str