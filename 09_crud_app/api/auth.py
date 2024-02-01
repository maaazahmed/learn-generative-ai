from fastapi import FastAPI
from pydantic import BaseModel

from ..db.query import *

class UserData(BaseModel):
    first_name:str
    last_name:str
    email:str
    password:str

# print(query)

app:FastAPI = FastAPI()

@app.post("/create-user")
def index(user:UserData)->dict:
    return {"message":"User created successfully","data":user}



