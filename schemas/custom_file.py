from pydantic import BaseModel
from datetime import datetime

class CustomFile(BaseModel):
    name: str
    creation_date: datetime
    size: int