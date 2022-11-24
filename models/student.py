from uuid import uuid4
from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    #id:str(uuid4())
    #id:Optional[str]
    name:str
    lastname:str
    clave:str
    
    