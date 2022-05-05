from pydoc import describe
from pydantic import BaseModel # helps to auto create json schema from model

class Todo(BaseModel):
    title: str
    description: str