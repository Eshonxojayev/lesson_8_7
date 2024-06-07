from pydantic import BaseModel
from typing import Optional

class JwtModel(BaseModel):
    authjwt_secret_key: str = '3ab42577ea4c274120ac14a8cd6d9b307f0b17f94d39a074b5073efe9c9fdbcb'

class RegisterModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

class LoginModel(BaseModel):
    username: str
    password: str

class CategoryModel(BaseModel):
    id: Optional[int]
    name: str

class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float    
    category_id: int


class OrderModel(BaseModel):
    id: Optional[int]
    user_id: int
    product_id: int
    count: int
    order_status: str

class UserOrder(BaseModel):
    username: str