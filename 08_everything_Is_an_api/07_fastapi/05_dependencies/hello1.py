from fastapi import FastAPI , Depends, Query



def login(username:str = Query(None),password:str = Query(None)):
    if(username == "admin" and password == "admin"):
        return {"message":"login successful"}
    else :
        return {"message":"login failed"}
    

app:FastAPI = FastAPI()

@app.get("/login")
def login_api(user:dict = Depends(login)):
    return user