from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer


class AccountBase(BaseModel):
    password: str

class AccountCreate(AccountBase):
    username: str
    name: str
    address: str
    phone: str

class AccountUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None

class Account(AccountBase):
    id: int
    accountInfo: Customer = None

    class ConfigDict:
        from_attributes = True


