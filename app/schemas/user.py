from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str
    login: str
    registered_from: datetime

