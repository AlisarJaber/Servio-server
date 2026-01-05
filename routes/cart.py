

from fastapi import FastAPI, APIRouter, HTTPException, status, Header, Request

router = APIRouter()


# @router.post("/carts", response_model=Cart, status_code=status.HTTP_201_CREATED)
# def create_cart(cart_request: NewCartRequest, apiKey: str | None = Header(None)):
#     verify_api_key(apiKey)
#     check_product_ids(cart_request.productIds)
#     new_id = 1 if not carts else carts[-1].id + 1
#     real_cart = Cart(
#         id=new_id,
#         customerName=cart_request.customerName,
#         productIds=cart_request.productIds,
#         isPaid=False
#     )
#     carts.append(real_cart)
#     return real_cart

# @router.get("/carts", response_model=List[Cart] )
# def get_all_carts(apiKey: str | None = Header(None)):
#     verify_api_key(apiKey)
#     return carts

# @router.get("/carts/{cart_id}", response_model=Cart)
# def get_cart(cart_id: int, apiKey: str | None = Header(None)):
#     verify_api_key(apiKey)
#     for cart in carts:
#         if cart.id == cart_id:
#             return cart
#     raise HTTPException(status_code=404, detail="Cart not found")

# @router.patch("/carts/{cart_id}", response_model=Cart)
# def update_cart(cart_id: int, cart_update: CartPatch, apiKey: str | None = Header(None)):
#     verify_api_key(apiKey)
#     if cart_update.productIds is not None:
#         check_product_ids(cart_update.productIds)
#     for cart in carts:
#         if cart.id == cart_id:
#             if cart_update.productIds is not None:
#                 cart.productIds = cart_update.productIds
#             return cart
#     raise HTTPException(status_code=404, detail="Cart not found")

# @router.delete("/carts/{cart_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_cart(cart_id: int, apiKey: str | None = Header(None)):
#     verify_api_key(apiKey)
#     for cart in carts:
#         if cart.id == cart_id:
#             carts.remove(cart)
#             return
#     raise HTTPException(status_code=404, detail="Cart not found")

# @router.post("/carts/{cart_id}/pay", response_model=dict)
# def pay_cart(cart_id: int, apiKey: str | None = Header(None)):
#     verify_api_key(apiKey)
#     for cart in carts:
#         if cart.id == cart_id:
#             if not cart.productIds:
#                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cart is empty")
#             if cart.isPaid:
#                 raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Cart already paid")
#             cart.isPaid = True
#             return {"message": f"Cart {cart_id} paid successfully"}
#     raise HTTPException(status_code=404, detail="Cart not found")
