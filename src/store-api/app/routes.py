from fastapi import APIRouter, HTTPException
from typing import List, Optional

from app.models import Product, ProductCreate
import app.database

router = APIRouter(prefix="/products", tags=["Inventory"])


@router.post("/", response_model=Product, status_code=201)
def create_product(product_in: ProductCreate) -> Product:
    new_product = Product(
        id=database.PRODUCT_ID_COUNTER,
        name=product_in.name,
        price=product_in.price,
        stock=product_in.stock,
        category=product_in.category       
    )

    database.INVENTORY.append(new_product)
    database.PRODUCT_ID_COUNTER += 1
    return new_product



@router.get("/", response_model=List[Product])
def get_products(category: Optional[str] = None) -> List[Product]:
    if category:
        return [product for product in database.INVENTORY if product.category.lower() == category.lower()]

    return database.INVENTORY



@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    for product in database.INVENTORY:
        if product.id == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")    



@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product_in: ProductCreate) -> Product:
    for product in database.INVENTORY:
        if product.id == product_id:
            product.price = product_in.price
            product.stock = product_in.stock
            return product

    raise HTTPException(status_code=404, detail="Product not found")



@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int) -> None:
    for index, product in enumerate(database.INVENTORY):
        if product.id == product_id:
            del database.INVENTORY[index]
            return  
    
    raise HTTPException(status_code=404, detail="Product not found")
