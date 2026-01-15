from pydantic import BaseModel

class UserRequest(BaseModel):
    FirstName: str
    lastname: str
    address: str
    age: int
    gender: str
    email: str
    phone: str | None = None
    password: str
    role: str | None = None

    
class LoginRequest(BaseModel):
    email: str
    password: str
