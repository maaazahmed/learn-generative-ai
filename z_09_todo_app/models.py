from pydantic import BaseModel



class UserData(BaseModel):
    first_name:str
    last_name:str
    email:str
    password:str