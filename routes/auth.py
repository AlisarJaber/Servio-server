from fastapi import APIRouter, HTTPException, Depends, Response
from sqlmodel import Session, select
from models.user import User
from schemas.user import UserRequest, LoginRequest
from db import engine, get_session
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
import jwt, os, hashlib
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from auth_helper import get_user

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET:
    raise RecursionError("JWE_SECRET not set")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/api/users",
    tags=["auth"]
)

def hash_password(password: str) -> str:
    sha = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_context.hash(sha)

def verify_password(password: str, hashed_password: str) -> bool:
    sha = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_context.verify(sha, hashed_password)

def create_token(user_id: int):
    expire = datetime.utcnow() + timedelta(days=1)
    payload = {"sub": str(user_id), "exp": expire}
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

@router.get("/me")
def get_current_user(
    user_id: int = Depends(get_user),  
    session: Session = Depends(get_session)
):
    statement = select(User).where(User.id == user_id)
    result = session.exec(statement).first()

    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    return result 

@router.post("/signup")
def signup(user_req: UserRequest, response: Response):
    with Session(engine) as session:
        existing_user = session.exec(
            select(User).where(User.email == user_req.email)
        ).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = hash_password(user_req.password)

        new_user = User(
            FirstName=user_req.FirstName,
            lastname=user_req.lastname,
            address=user_req.address,
            age=int(user_req.age),
            gender=user_req.gender,
            email=user_req.email,
            password=hashed_password,
            role="user",
            is_admin=False
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        token = create_token(new_user.id)
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,
            samesite="lax"
        )

        return {
            "id": new_user.id,
            "email": new_user.email,
            "FirstName": new_user.FirstName
        }
        # data = user_req.model_dump(exclude_none=True)
        # data["age"] = int(data["age"])  
        # hashed_password = pwd_context.hash(data["password"])
        # data["password"] = hashed_password
        # new_user = User(**data, is_admin=False)
        # session.add(new_user)
        # session.commit()
        # session.refresh(new_user)
        # return {
        #     "id": new_user.id,
        #     "email": new_user.email,
        #     "FirstName": new_user.FirstName
        # }

def create_token(user_id: int):
    expire = datetime.utcnow() + timedelta(days=1)
    payload = {"sub": str(user_id), "exp": expire}
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

@router.post("/login")
def login(loginRequest: LoginRequest, response: Response):
    req_dict = loginRequest.model_dump()
    with Session(engine) as session:
        statement = select(User).where(User.email == req_dict["email"])
        user = session.exec(statement).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        if not verify_password(req_dict["password"], user.password):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        token = create_token(user.id)
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,
            samesite="lax"
        )
        return user
    # req_dict = loginRequest.model_dump()
    # with Session(engine) as session:
    #     statement = select(User).where(User.email == req_dict["email"])
    #     user = session.exec(statement).first()
    #     if user is None:
    #         raise HTTPException(status_code=401, detail="Invalid email or password")
    #     is_password_match = pwd_context.verify(req_dict["password"], user.password)
    #     if not is_password_match:
    #         raise HTTPException(status_code=401, detail="Invalid email or password")
    #     token = create_token(user.id)
    #     response.set_cookie(key="access_token", value=token, httponly=True, samesite="lax")
    #     return {"user": {"id": user.id, "email": user.email}}


        


        


