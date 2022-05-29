from distutils.command.config import config
from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

from sqlalchemy import true

class userInput(BaseModel):
    email:EmailStr
    first_name:str
    last_name:str
    password:str

    class config:
        orm_mode:true