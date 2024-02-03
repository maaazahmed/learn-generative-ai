from  table import User,Todo, Base
from  connection import engine, db, Session



class TableHandlers:
    def create_table(self):
        Base.metadata.create_all(bind=engine)



class AuthHadlers:
    def create_user(self):
          session:Session = Session()
          new_user = User(
             first_name="Maaz",
             last_name="Ali",
             email="maasssa@gmail.com",
             password="XXXX"
        )
          session.add_all([new_user])
          session.commit()
      
             


# AuthHadlers().create_user()














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
