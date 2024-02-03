from fastapi import FastAPI,Body, Depends 
from query import AuthHadlers
from models import UserData
from typing import Annotated



app:FastAPI = FastAPI()
authHadlers:AuthHadlers = AuthHadlers()


def signup(user:UserData = Body(embed=True))->dict:
    response = authHadlers.create_user(user=user.model_dump())
    return response 


def login(user:UserData = Body(embed=True))->dict:
    response = authHadlers.login(user=user.model_dump())
    return response


@app.post("/create-user")
def create_new_user(user:Annotated[dict, Depends(signup)])->dict:
    return user


@app.post("/login")
def login_user(loginData:Annotated[dict, Depends(login)])->dict:
     return loginData




# @app.post("/create-user")
# def index(user:UserData = Body(embed=True))->dict:
#     response = authHadlers.create_user(user=user.model_dump())
#     return response


# conda activate python-env-12

