# from sqlmodel import  Field,Session, SQLModel, create_engine


# from typing import Optional


# class Hero(SQLModel, table=True):
#     id:Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     secret_name: str
#     age:Optional[int] = None



# hero_1 = Hero(name="Maaz", secret_name="ahmed")
# hero_2 = Hero(name="Aslam", secret_name="Ali")
# hero_3 = Hero(name="Ali", secret_name="Ahmed", age=20)


# engine =  create_engine("postgresql://maaazahmed:ySmszr3GV7jp@ep-late-scene-a1ra8ckq.ap-southeast-1.aws.neon.tech/neondb?sslmode=require")


# SQLModel.metadata.create_all(engine)



# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()



from fastapi import  FastAPI, Depends
from sqlmodel import SQLModel,Field,Session, create_engine, select
from typing import Annotated


app:FastAPI = FastAPI(version="1.0.0", title="Location API", servers=[
    {
        "url":"http://localhost:8000",
        "description":"Local server"
    }
])


engine =  create_engine("postgresql://maaazahmed:ySmszr3GV7jp@ep-late-scene-a1ra8ckq.ap-southeast-1.aws.neon.tech/neondb?sslmode=require")

class Location (SQLModel,table=True):
    name:str  = Field(index=True, primary_key=True)
    location:str
 

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def create_db():
    create_db_and_tables()



@app.post("/persons")
def create_person(person_data:Location):
    with Session(engine) as session:
        session.add(person_data)
        session.commit()
        session.refresh(person_data)
        return person_data
    



@app.get("/persons")
def get_persons():
    with Session(engine) as session:
        loc_data  =  session.exec(select(Location)).all()
        return loc_data



def get_location_or_404(name:str)->Location:
    with Session(engine) as session:
        loc_data = session.exec(select(Location).where(Location.name == name)).first()
        return loc_data


 
@app.get("/location/{name}")
def get_person(name:str, location:Annotated[Location, Depends(get_location_or_404)]):
    return location

        


