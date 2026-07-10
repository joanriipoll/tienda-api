from typing import List, Optional
from sqlmodel import Session, select
from app.models import ProductDBModel
from app.entities import ProductCreate, ProductEntity

class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, product_in: ProductCreate) -> ProductEntity:
        db_product = ProductDBModel(**product_in.model_dump())
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return ProductEntity(**db_product.model_dump())



    def get_all(self, category: Optional[str] = None) -> List[ProductEntity]:
        statement = select(ProductDBModel)
        if category: 
            statement = statement.where(ProductDBModel.category.ilike(category)) 
        db_products = self.session.exec(statement).all()
        return [ProductEntity(**p.model_dump()) for p in db_products]



    def find_by_id(self, product_id: int) -> Optional[ProductEntity]:
        db_product = self.session.get(ProductDBModel, product_id)
        if not db_product:
            return None
        return ProductEntity(**db_product.model_dump())
    


    def update(self, product_id: int, product_in: ProductCreate) -> Optional[ProductEntity]:
        db_product = self.session.get(ProductDBModel, product_id)
        if not db_product:
            return None
        db_product.price = product_in.price
        db_product.stock = product_in.stock
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return ProductEntity(**db_product.model_dump())
    


    def delete(self, product_id: int) -> bool:
        db_product = self.session.get(ProductDBModel, product_id)
        if not db_product:
            return False
        self.session.delete(db_product)
        self.session.commit()
        return True
