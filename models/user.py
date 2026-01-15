from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__="users"
    id: int | None = Field(default=None, primary_key=True)
    FirstName: str
    lastname: str
    address: str
    age: int
    role: str =  Field(default="user")
    gender: str
    email: str = Field(unique=True)
    is_admin: bool = Field(default=False)
    password: str
