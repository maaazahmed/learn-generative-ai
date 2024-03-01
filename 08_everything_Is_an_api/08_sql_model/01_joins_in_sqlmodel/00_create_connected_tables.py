from sqlmodel import Field, SQLModel, create_engine, Session, select, delete, Relationship
from typing import Optional


class Team(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    headquarters:str
    heroes:list["Hero"] = Relationship(back_populates="team")
   

class Hero(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    secret_name:str
    age:Optional[int] =  Field(index=True)      
    team_id:Optional[int] = Field(default=None, foreign_key="team.id")
    team:Optional[Team] = Relationship(back_populates="heroes")







# =>> DATABASE URL <<= #
db_url = "postgresql://maaazahmed:ySmszr3GV7jp@ep-late-scene-a1ra8ckq.ap-southeast-1.aws.neon.tech/sql-model?sslmode=require"
engine = create_engine(db_url, echo=True)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def create_heros():
    with Session(engine) as session:
        print("-----------------------------------------------------------------------------------------------")
        teme1 = Team(name="Preventers", headquarters="Sharp Tower")
        teme2 = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        session.add(teme1)
        session.add(teme2)
        session.commit()

        hero_deadpond =  Hero(name="Deadpond", secret_name="Dive Wilson",age=10, team_id=teme2.id)
        hero_rusty_man =  Hero(name="Rusty-Man", secret_name="Tommy Sharp", team_id=teme1.id)
        hero_spider_boy =  Hero(name="spider-boy", secret_name="spider boy", team_id=teme2.id)

        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        # hero_spider_boy.team_id =  teme1.id
        # session.add(hero_spider_boy)
        # session.commit()
        # session.refresh(hero_spider_boy)


        # hero_spider_boy.team_id = teme1.id
        # session.add(hero_spider_boy)
        # session.commit()
        # session.refresh(hero_spider_boy)



        print("deadpond",  hero_deadpond)
        print("rusty",  hero_deadpond)
        print("spider_boy",  hero_deadpond)
        print("-----------------------------------------------------------------------------------------------")


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



def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        hero = session.exec(statement).one()
        hero.age = 120
        session.add(hero)
        session.commit()
        session.refresh(hero)
        # session.add(res)
        # session.commit()
        # session.refresh(res)
        
        print("========================= \n T E S T \n",hero,"\n T E S T \n =========================")


       
def  delete_heroes():
    with Session(engine) as session:
        # st = delete(Hero)
        # session.exec(st)
        dt = delete(Hero)
        dh = delete(Team)
        session.exec(dt)
        session.exec(dh)
        session.commit()




def create_team_with_relation():
    print("====================")
    with Session(engine) as session:
        react_team = Team(name="React Developers", headquarters="React office")
        team_python = Team(name="Python Developer", headquarters="Python office")

        hero_1 =  Hero(name="Maaz Ahmed", secret_name="react-developer", team=react_team)
        hero_2 =  Hero(name="Aslam Khan", secret_name="python developer", team=react_team)


        # session.add(hero_1)
        # session.add(hero_2)
        # session.commit()
        # session.refresh(hero_1)
        # session.refresh(hero_2)

        hero_1.team = react_team
        session.add(hero_1)
        session.commit()
        session.refresh(hero_1)

        



        # session.add_all([team_python, react_team, hero_1, hero_2])
        # session.commit()
     



# def update_team_with_relation():
#     with Session(engine) as session:


        


def get_heroses ():
    with Session(engine) as session:
        statement =  select(Hero).where(Hero.name == "Maaz Ahmed")
        result = session.exec(statement)
        res_hero = result.first()
        print("====================")
        print("Hero ",res_hero, "")
        print("____________________")
        print("Hero ",res_hero.team, "")
        print("____________________")
        print("====================")
        print("--------------------")
        statement_2 = select(Team).where(Team.id == res_hero.team_id)
        result_2 = session.exec(statement_2).first()
        print("====================")
        print("Tem ",result_2, "")
        print("====================")

        
        






def main():
    # create_db_and_table()    
    # create_heros()
    # select_heroes()
    # select_heroes_with_join()
    # delete_heroes()
    # update_heroes()
    # create_team_with_relation()
    get_heroses()



















    



if __name__ in "__main__":
    main()







