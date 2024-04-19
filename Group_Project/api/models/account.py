from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, autoincrement=True)
    username = Column(String(100), ForeignKey("customers.email"), primary_key=True, index=True)
    password = Column(String(100), index=True)
    name = Column(String(100), ForeignKey("customers.name"))
    address = Column(String(100), ForeignKey("customers.address"))
    phone = Column(String(100), ForeignKey("customers.phone"))

    customers = relationship("Customer", back_populates="accounts")