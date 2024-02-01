from fastapi import FastAPI, Depends

from typing import Annotated
def depfunc1(num:int): 
    num = int(num)
    num += 1
    return num

def depfunc2(num): 
    num = int(num)
    num += 1
    return num


app:FastAPI = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])

@app.get("/main/{num}")
def main(num:int, num1:Annotated[int, Depends(depfunc1)], num2:Annotated[int, Depends(depfunc2)]):
    total = num + num1 + num2
    return total