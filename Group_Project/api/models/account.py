from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, autoincrement=True)
    account_username = Column(String(100), ForeignKey("customers.email"), primary_key=True, index=True)
    account_password = Column(String(100), index=True)
    account_name = Column(String(100), ForeignKey("customers.name"))
    account_address = Column(String(100), ForeignKey("customers.address"))
    account_phone = Column(String(100), ForeignKey("customers.phone"))

    customers = relationship("Customer", back_populates="accounts")