from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str
    price: float = Field(gt=0, description="The price must be greater than zero.")
    stock: int = Field(ge=0, description="The stock must be greater than or equal to zero.")
    category: str

class ProductEntity(ProductCreate):
    id: int