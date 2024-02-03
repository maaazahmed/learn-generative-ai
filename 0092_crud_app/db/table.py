from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column, relationship
from  sqlalchemy import ForeignKey



class Base(DeclarativeBase):
    pass



class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    first_name:Mapped[str] = mapped_column(nullable=False)
    last_name:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False, unique=True)
    password:Mapped[str] = mapped_column(nullable=False)
    todos:Mapped[list["Todo"]] = relationship(backref="user", passive_deletes=True)

    def __repr__(self) -> str:
        return f'< {f"{self.first_name} {self.last_name}"} >'




class Todo(Base):
    __tablename__ = "todos"
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(nullable=False)
    description:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    def __repr__(self) -> str:
        return f'< {self.title} >'
