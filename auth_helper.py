from fastapi import Cookie, HTTPException
import jwt, os
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET not set in .env")

def get_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        print(access_token, JWT_SECRET )
        payload = jwt.decode(access_token, 
        JWT_SECRET, "HS256")
        print("payload is",payload)
        user_id = payload.get("sub")
        print("auth helper user id", user_id)

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    # except jwt.PyJWTError:
    #     raise HTTPException(status_code=401, detail="Invalid token")

