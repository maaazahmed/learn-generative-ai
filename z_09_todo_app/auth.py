from fastapi import FastAPI,Body, Depends 
from query import AuthHadlers
from models import UserData
from typing import Annotated



app:FastAPI = FastAPI()

authHadlers:AuthHadlers = AuthHadlers()


def login_user(user:dict = Body(None))->dict:
    # response = authHadlers.login(user=user)
    # return response
    return {"message":"user logedin"}




@app.post("/create-user")
def index(user:Annotated[dict, Depends(login_user)])->dict:
    return user
    # response = authHadlers.create_user(user=user.model_dump())
    # return response


# @app.post("/create-user")
# def index(user:UserData = Body(embed=True))->dict:
#     response = authHadlers.create_user(user=user.model_dump())
#     return response


# conda activate python-env-12

