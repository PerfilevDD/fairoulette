from sqlalchemy import Column, String, Float, Integer

from database.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    balance = Column(Integer) # Guthaben in cent
    
class Bet(Base):
    __tablename__ = "bet"

    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer)
    user_id = Column(Integer)

    type = Column(String, nullable=False)
    value = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

class RouletteTable(Base):
    __tablename__ = "roulette_table"
    id = Column(Integer, primary_key=True, index=True)

class BalanceUpdate(Base):
    bet_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    table_id = Column(Integer, primary_key=True)

    bet_earnings = Column(Integer)





