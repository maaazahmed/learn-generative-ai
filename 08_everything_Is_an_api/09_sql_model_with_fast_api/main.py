from sqlmodel import create_engine,select, Session, SQLModel
from fastapi import FastAPI, Depends, HTTPException, status
from model import UserResponse, UserCreate,User, UserLogin, Token, TokenData
from typing import Annotated
from service import get_hashed_pass, verify_password,create_access_token, verify_token,ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta


app:FastAPI =  FastAPI()

db_url = "postgresql://maaazahmed:ySmszr3GV7jp@ep-late-scene-a1ra8ckq.ap-southeast-1.aws.neon.tech/sql-model?sslmode=require"
engine = create_engine(db_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


def get_deb():
    with Session(engine) as session:
        return session




@app.post("/signup", response_model=Token)
async def create_user(user:UserCreate, db:Annotated[Session, Depends(get_deb)]):
    statement = select(User).where(User.email == user.email)
    is_user = db.exec(statement).first()
    if is_user is not None :
        raise HTTPException(status_code=404, detail="Email already in use!")
    else:    
        user.password = get_hashed_pass(user.password)
        validate_user = User.model_validate(user)
        db.add(validate_user)
        db.commit()
        db.refresh(validate_user)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"email":validate_user.email}, expires_delta=access_token_expires)
        return Token(access_token=access_token, token_type="bearer")
    





@app.post("/login", response_model=Token)
async def login_user(login_data:UserLogin, db:Annotated[Session,Depends(get_deb)]):
    statement = select(User).where(User.email == login_data.email)
    user = db.exec(statement).first()
    if user is not None:
        if not verify_password(login_data.password,user.password):
            raise HTTPException(status_code=404, detail="Invalid email or password!") 
        else:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(data={"email":user.email}, expires_delta=access_token_expires)
            return Token(access_token=access_token, token_type="bearer")
    else:
        raise HTTPException(status_code=404, detail="User not found") 






@app.get("/user", response_model=UserResponse)
async def get_user(db:Annotated[Session, Depends(get_deb)],token_data:Annotated[TokenData, Depends(verify_token)]):
    print("token: ", token_data)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticat":"Bearer"}
    )
    if token_data.email is None:
        raise credentials_exception
    statement = select(User).where(User.email == token_data.email)
    response = db.exec(statement).one()
    if not response:
        raise credentials_exception
    return response








    









# from fastapi import FastAPI, Depends, HTTPException, Query
# from typing import Annotated
# from sqlmodel import  Field, SQLModel, create_engine, Session, select



# class HeroBase(SQLModel):
#     name:str = Field(index=True)
#     secret_name:str


# class Hero(HeroBase, table=True):
#     id:int | None  = Field(default=None, primary_key=True)
#     age:int | None = None


# class HeroCreate(HeroBase):
#     age:int | None= None


# class HeroResponse(HeroBase):
#     id:int
#     age:int | None = None



# class HeroUpdate(SQLModel): 
#     name:str | None = None
#     secret_name:str | None = None
#     age:int  | None = None




# app:FastAPI = FastAPI()

# db_url = "postgresql://maaazahmed:ySmszr3GV7jp@ep-late-scene-a1ra8ckq.ap-southeast-1.aws.neon.tech/sql-model?sslmode=require"

# engine = create_engine(db_url, echo=True)


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)



# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()



# def get_deb():
#    with Session(engine) as session:
#        yield session


# @app.get("/heroes", response_model=list[Hero])
# # async def red_heroes(session:Annotated[Session, Depends(get_deb)], offset:int, limit:int):
# async def red_heroes(session:Annotated[Session, Depends(get_deb)], offset:int= Query(default=0, le=4), limit:int = Query(default=0, le=4)):
#    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
#    return heroes



# @app.post("/heroes", response_model=HeroResponse)
# def add_hero(hero:HeroCreate, db:Annotated[Session, Depends(get_deb)]):
#     validate_hero = Hero.model_validate(hero)
#     db.add(validate_hero)
#     db.commit()
#     db.refresh(validate_hero)
#     return validate_hero



# @app.get("/heroes/{hero_id}")
# async def get_hero(hero_id:int, session:Annotated[Session, Depends(get_deb)]):
#    hero = session.get(Hero, hero_id)
#    if not hero:
#        raise HTTPException(status_code=404, detail="hero not found")
#    else:
#        return hero





# @app.patch("/heroes/{hero_id}")
# async def update_hero(hero_id:int, hero_data:HeroUpdate, session:Annotated[Session, Depends(get_deb)]):
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="hero not found")
#     hero_dict = hero_data.model_dump(exclude_unset=True)
#     for key, value in hero_dict.items():
#         setattr(hero, key, value)
#     session.add(hero)
#     session.commit()
#     session.refresh(hero)
#     return hero
    

#     # session.exec(update(Hero).where(Hero.id == 62).values(name="Aslam", age=12))
    
#     # session.commit()
#     # session.refresh()
#     # return hero_data


    

