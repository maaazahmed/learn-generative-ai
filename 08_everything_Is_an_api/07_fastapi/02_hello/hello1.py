
from fastapi import FastAPI

app:FastAPI = FastAPI()


# @app.get("/hi")
# def greet()->str:
#     return "How are you"




@app.get("/hi")
def greet()->dict:
    return{"message":"How are you"}



@app.get("/hi/{name}")
def green_name(name:str)->dict:
    return {"message":f"How are you, {name}"}

