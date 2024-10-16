from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property

class Product (db.Model):
    __tablename__ = 'product'
    __id = db.Column("id",db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column("name",db.String(50))
    __price = db.Column("price",db.String(50))
    __brand = db.Column("category",db.String(50))
    __size = db.Column("size",db.String(50))
    __stock = db.Column("stock",db.String(50))
    
    def __init__(self, name, price, brand, size, stock, id=None):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__brand = brand
        self.__size = size
        self.__stock = stock


    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id:int):
        self.__id = id

    @hybrid_property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self, name:str):
        self.__name = name

    @hybrid_property
    def price(self)->str:
        return self.__price
    
    @price.setter
    def price(self, price:str):
        self.__price = price

    @hybrid_property
    def brand(self)->str:
        return self.__brand
    
    @brand.setter
    def brand(self, brand:str):
        self.__brand = brand

    @hybrid_property
    def size(self)->str:
        return self.__size
    
    @size.setter
    def size(self, size:str):
        self.__size = size

    @hybrid_property
    def stock(self)->str:
        return self.__stock
    
    @stock.setter
    def stock(self, stock:str):
        self.__stock = stock

    def __repr__(self):
        return f'Product: {self.id} {self.name} {self.price} {self.brand} {self.size} {self.stock}'
    
    def __eq__(self, o:object) -> bool:
        return self.__id==o.id and self.__name==o.name

    