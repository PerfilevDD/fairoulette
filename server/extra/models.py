from sqlalchemy import Column, String, Float, Integer

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    balance = Column(Float)
    
class Bet(Base):
    __tablename__ = "bet"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    type = Column(String, nullable=False)
    value = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
