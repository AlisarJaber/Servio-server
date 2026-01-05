from fastapi import FastAPI, APIRouter, HTTPException, status, Header, Request
from typing import List
from models.cart import Cart, NewCartRequest, CartPatch
from data.carts import carts
from data.products import products
from data.apiKey import myapiKey
from fastapi.responses import JSONResponse
from routes.product import router as productRouter



def check_product_ids(product_ids: List[int]):
    valid_ids = [product["id"] for product in products]
    for pid in product_ids:
        if pid not in valid_ids:
            raise HTTPException(status_code=404, detail=f"Product {pid} not found")

def verify_api_key(apiKey: str | None):
    if apiKey is None or apiKey != myapiKey:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Api key")
    

app = FastAPI()

@app.middleware("http")
async def basic_middleware(request, call_next):
    print("HEADERS:")
    print(dict(request.headers))

    body = await request.body()
    print("BODY:")
    print(body.decode("utf-8"))

    async def receive():
        return {"type": "http.request", "body": body}

    request._receive = receive

    response = await call_next(request)
    return response

@app.middleware("http")
async def api_key_middleware(request, call_next):
    api_key_header = request.headers.get("apikey")
    if not api_key_header or api_key_header != myapiKey:
            return JSONResponse(
                status_code=401,
                content={"detail": "wrong credentials"}
            )
    response = await call_next(request)
    return response


app.include_router(productRouter, prefix="/api/products")
