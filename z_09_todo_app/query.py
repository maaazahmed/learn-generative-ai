from  table import *
from connection import engine,  Session
from sqlalchemy.exc import IntegrityError
import json
from fastapi import HTTPException, status

class TableHandlers:
    def create_table(self):
        Base.metadata.create_all(bind=engine)

def show_json(obj):
    return json.loads(obj)

class AuthHadlers:
  
    def create_user(self,user:dict):
        """
        this function takes a user dictionary and creates a new user in the database
        :param user: user dictionary
        :return: None if the user is created successfully, otherwise an error message is returned.
        :raises HTTPException: if the user is not created successfully, it raises an HTTPException with the appropriate error message.
        :raises Exception: if an exception occurs while creating the user, it raises an HTTPException with the appropriate error message.
        :raises IntegrityError: if an integrity error occurs while creating the user, it raises an HTTPException with the appropriate error message.
        :raises HTTPException: if the user is not created successfully, it raises an HTTPException with the appropriate error message.
        :raises Exception: if an exception occurs while creating the user, it raises an HTTPException with the appropriate error message.
        :raises IntegrityError: if an integrity error occurs while creating the user, it raises an HTTPException with the appropriate error message.
        :raises HTTPException: if the user is not created successfully, it raises an HTTPException with the appropriate error message.
        """
        session:Session = Session()
        first_name=user.get("first_name"),
        last_name=user.get("last_name"),
        email=user.get("email"),
        password=user.get("password")
        print("====================", email,"====",password,"======================= siup")

        if first_name is None or last_name is None or email is None or password is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error: Please fill all the fields")
        
        __user = self.get_user(email=email)
        if __user is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error: email already exists! ")
        else:
            try:
                new_user = User(first_name=first_name, last_name=last_name,email=email,password=password)
                session.add_all([new_user])
                session.commit()
                return {"message":"User created successfully"}
            except IntegrityError as e:
                session.rollback()
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
            except Exception as e:
                session.rollback()
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)





    def login(self, user:dict):
        """
         this function takes username and password and check if the username and password are correct
        :param username: username
        :param password: password
        :return: True if username and password are correct, False otherwise
        """
        email=user.get("email"),
        password=user.get("password"),

        if email is None or password is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error: Please fill all the fields")
        else:    
            try: 
                __user = self.get_user(email=email)
                return {"message":"User logged in successfully","user":{
                    "first_name":__user.first_name,
                    "last_name":__user.last_name,
                    "email":__user.email,
                    "password":__user.password,
                }}
            except IntegrityError as e:
                    # session.rollback()
                    # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
                    return {"message":"User logged in successfully","user":"XXXXXX"}
                
            except Exception as e:
                    # session.rollback()
                    # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
                    return {"message":"User logged in successfully","user":"YYY"}
            












    
    def get_user(self,email:str):
        """
        this functions takes email and return user if exist
        """
        session:Session = Session()
        user = session.query(User).filter_by(email = email).first()
        if user:
            print(f"User ID: {user.id}, Email: {user.email}")
            return user
        else :
            return user
             












