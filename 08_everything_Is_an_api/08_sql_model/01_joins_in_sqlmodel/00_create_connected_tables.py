from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional

class Team(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    headquarters:str


class Hero(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    secret_name:str
    age:Optional[int] =  Field(index=True)      
    team_id:Optional[int] = Field(default=None, foreign_key="team.id")



# =>> DATABASE URL <<= #
db_url = "postgresql://maaazahmed:ySmszr3GV7jp@ep-late-scene-a1ra8ckq.ap-southeast-1.aws.neon.tech/sql-model?sslmode=require"

engine = create_engine(db_url, echo=True)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def create_heros():
    with Session(engine) as session:
        teme1 = Team(name="Preventers", headquarters="Sharp Tower")
        teme2 = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        session.add(teme1)
        session.add(teme2)
        session.commit()

        hero_deadpond =  Hero(name="Deadpond", secret_name="Dive Wilson",age=10, team_id=teme2.id)
        hero_rusty_man =  Hero(name="Rusty-Man", secret_name="Tommy Sharp", team_id=teme1.id)
        hero_spider_boy =  Hero(name="Rusty-Man", secret_name="Tommy Sharp", team_id=teme2.id)

        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("deadpond",  hero_deadpond)
        print("rusty",  hero_deadpond)
        print("spider_boy",  hero_deadpond)



def select_heroes():
    with Session(engine) as session:
        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        resulet = session.exec(statement)
        for hero, team in resulet:
            print("hero => ", hero.name, "|| Team => ", team.name)



def select_heroes_with_join():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team, isouter=True).where(Team.name == "Preventers")
        res = session.exec(statement)
        for hero, team in res:
            print(hero.name,"=====",team.name)
       


def main():
    # create_db_and_table()    
    # create_heros()
    select_heroes()
    select_heroes_with_join()



if __name__ in "__main__":
    main()







