from  table import *
from connection import engine, db, Session
from sqlalchemy.exc import IntegrityError
import json
from models import UserData
from sqlalchemy import select

# from .models import A

class TableHandlers:
    def create_table(self):
        Base.metadata.create_all(bind=engine)





# def formValidate(first_name, last_name, email, password):
#     # Check if any of the fields are empty
#         print("All fields are required. Please fill in all the information.")
#     else:
#         # Check if the email has a valid format (this is a basic example)
#         if "@" not in email or "." not in email:
#             print("Invalid email format. Please provide a valid email address.")
#         else:
#             # Check if the password meets certain criteria (this is a basic example)
#             if len(password) < 6:
#                 print("Password must be at least 6 characters long.")
#             else:
#                 # All validations passed, proceed with sign-up logic
#                 # For example, you might want to save the user to a database
#                 # save_user_to_database(first_name, last_name, email, password)
#                 # print("Sign-up successful!")
#                 return True

def show_json(obj):
    return json.loads(obj)


class AuthHadlers:
    def create_user(self,user:dict):
        print("................... ACCOUNT CREATING........................")
        print(user.get("first_name"))
        print(user.get("last_name"))
        print(user.get("email"))
        print(user.get("password"))
        print("................... ACCOUNT CREATING........................")
       
        session:Session = Session()
        first_name=user.get("first_name"),
        last_name=user.get("last_name"),
        email=user.get("email"),
        password=user.get("password")

        __user = self.get_user(email=email)
        print(__user is not None,"__user is not None")
        if __user is not None:
            print("============== ERROR ============")
            print({"message":"User already exists"})
            print("============== ERROR ============")
            return {"message":"User already exists"}
        else:
            print("============== ACCOUNT CREATING ============")
            try:
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                session.add_all([new_user])
                session.commit()
                print("============== SUCCESS ============")
                print({"message":"User created sucxcessfully"})
                print("============== SUCCESS ============")
                return {"message":"User created successfully"}
            except IntegrityError as e:
                # session.rollback()
            # print("============== ERROR ============")
                return({"message":f"Error: email already exists ", "error":e})
            # print("============== ERROR ============")
            except Exception as e:
                print("============== ERROR ============")
                print(f"An unexpected error occurred: {e}")
                print("============== ERROR ============")
        
        

        

        

        
        

        # _usr = {
        #         "id":__user.id,
        #             "first_name":__user.first_name,
        #             "last_name":__user.last_name,
        #             "email":__user.email,
        #             "password":__user.password
        #         }
    



    def get_user(self,email:str):
        session:Session = Session()
        user = session.query(User).filter_by(email = email).first()

        # user =  session.query(User).where(User.email == email).first()
        # stmt = select(User).where(User.email == email).all()
        # all_users = session.query(User).all()
        print(user,"USER =>")
        



        if user:
            print(f"User ID: {user.id}, Email: {user.email}")
            print("============== SUCCESS ============")
            print({"message":"User found successfully","user":user})
            print("============== SUCCESS ============")
            return {"message":"User found successfully","user":user}
        else :
            print("============== ERROR ============")
            print({"message":"User not found"})
            print("============== ERROR ============")
            return {"message":"User not found"}

        
      

             


# AuthHadlers().get_user(email="maaaxx@gmail.com")














# {
#  "cells": [
#   {
#    "cell_type": "code",
#    "execution_count": 8,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "from  table import Base, User, Todo\n",
#     "from  connection import engine, db, Session\n",
#     "\n",
#     "\n",
#     "\n",
#     "class TableHandlers:\n",
#     "    def create_table(self):\n",
#     "        Base.metadata.create_all(bind=engine)\n",
#     "\n",
#     "\n",
#     "\n",
#     "class AuthHadlers:\n",
#     "    def create_user(self):\n",
#     "          session:Session = Session()\n",
#     "          new_user = User(\n",
#     "             first_name=\"Maaz\",\n",
#     "             last_name=\"Ali\",\n",
#     "             email=\"maasa@gmail.com\",\n",
#     "             password=\"XXXX\"\n",
#     "        )\n",
#     "          session.add_all([new_user])\n",
#     "          session.commit()\n",
#     "      \n",
#     "             \n",
#     "\n",
#     "\n",
#     "AuthHadlers().create_user()"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 9,
#    "metadata": {},
#    "outputs": [],
#    "source": []
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 11,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stdout",
#      "output_type": "stream",
#      "text": [
#       "2024-01-21 02:06:52,871 INFO sqlalchemy.engine.Engine BEGIN (implicit)\n",
#       "2024-01-21 02:06:52,872 INFO sqlalchemy.engine.Engine INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s) RETURNING users.id\n",
#       "2024-01-21 02:06:52,873 INFO sqlalchemy.engine.Engine [cached since 44.2s ago] {'first_name': 'Maaz', 'last_name': 'Ali', 'email': 'maasa@gmail.com', 'password': 'XXXX'}\n",
#       "2024-01-21 02:06:53,051 INFO sqlalchemy.engine.Engine COMMIT\n"
#      ]
#     }
#    ],
#    "source": [
#     "\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": []
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "python-env-12",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.12.0"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 2
# }
