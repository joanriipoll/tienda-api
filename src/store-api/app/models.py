from typing import Optional
from sqlmodel import SQLModel, Field

class ProductDBModel(SQLModel, table=True):
    __tablename__ = "products"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    price: float
    stock: int
    category: str