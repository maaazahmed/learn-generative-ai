from pydantic import BaseModel



class UserData(BaseModel):
    first_name:str | None = None
    last_name:str | None = None
    email:str 
    password:str 