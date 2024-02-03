from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session


conn_str = f'postgresql://maaazahmed:ySmszr3GV7jp@ep-late-scene-a1ra8ckq.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'
engine:Engine = create_engine(conn_str, echo=True)
Session = sessionmaker(bind=engine)
db:Session = Session()

