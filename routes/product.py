
from fastapi import APIRouter
from data.products import products 
router = APIRouter()

@router.get("/")
def get_products():
    return products

