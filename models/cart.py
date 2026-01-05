from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

class Cart(BaseModel):
    id: int
    customerName: str
    productIds: List[int]
    isPaid: bool

class NewCartRequest(BaseModel):
    customerName: str
    productIds: List[int]

class CartPatch(BaseModel):
    productIds: Optional[List[int]] = None