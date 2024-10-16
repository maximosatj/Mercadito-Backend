from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property

class Order(db.Model):
    __tablename__ = 'orders'
    __id_order = db.Column("id",db.Integer, primary_key=True)
    __id_client = db.Column("id_client",db.String(50))
    __id_product = db.Column("id_product",db.String(50))
    __payment_method = db.Column("payment_method",db.String(50))
    __total = db.Column("total",db.String(50))
    
    def __init__(self, id_order, id_client, id_product, payment_method, total):
        self.__id_order = id_order
        self.__id_client = id_client
        self.__id_product = id_product
        self.__payment_method = payment_method
        self.__total = total
        
    @hybrid_property
    def id_order(self)->str:
        return self.__id_order
    
    @id_order.setter
    def id_order(self, id_order:str):
        self.__id_order = id_order
        
    @hybrid_property
    def id_client(self)->str:
        return self.__id_client
    
    @id_client.setter
    def id_client(self, id_client:str):
        self.__id_client = id_client
    
    @hybrid_property
    def id_product(self)->str:
        return self.__id_product
    
    @id_product.setter
    def id_product(self, id_product:str):
        self.__id_product = id_product
        
    @hybrid_property
    def payment_method(self)->str:
        return self.__payment_method
    
    @payment_method.setter
    def payment_method(self, payment_method:str):
        self.__payment_method = payment_method

    @hybrid_property
    def total(self)->str:
        return self.__total
    
    @total.setter
    def total(self, total:str):
        self.__total = total
    
    def __repr__(self):
        return f"Operations (id_operation{self.__id_order}, {self.__id_user}, {self.__id_product}, {self.__payment_method}, {self.__total})"
    
    def __eq__(self, o:object) -> bool:
        return self.__id_order==o.id and self.__total==o.total