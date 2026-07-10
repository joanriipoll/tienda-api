from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.entities import ProductCreate, ProductEntity
from app.repositories import ProductRepository
from app.database import get_session

router = APIRouter(prefix="/products", tags=["Products"])

def get_product_repository(session: Session = Depends(get_session)) -> ProductRepository:
    return ProductRepository(session)


@router.post("/", response_model=ProductEntity, status_code=status.HTTP_201_CREATED)
def create_product(
    product_in: ProductCreate, 
    repository: ProductRepository = Depends(get_product_repository)
):
    return repository.save(product_in)



@router.get("/", response_model=List[ProductEntity])
def get_products(
    category: Optional[str] = None,
    repository: ProductRepository = Depends(get_product_repository)
):
    return repository.get_all(category=category)



@router.get("/{product_id}", response_model=ProductEntity)
def get_product(
    product_id: int, 
    repository: ProductRepository = Depends(get_product_repository)
):
    product = repository.find_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product



@router.put("/{product_id}", response_model=ProductEntity)
def update_product(
    product_id: int, 
    product_in: ProductCreate,
    repository: ProductRepository = Depends(get_product_repository)
):
    updated_product = repository.update(product_id, product_in)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int, 
    repository: ProductRepository = Depends(get_product_repository)
):
    success = repository.delete(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return None