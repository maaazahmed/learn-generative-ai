# imort """Base""" class from  table.py 
# from pydantic import BaseModel
from fastapi import FastAPI

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("auth:app", reload=True)