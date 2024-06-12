from sqlalchemy.orm import Session

import database.models as models
import database.schemas as schemas


def get_user_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_user_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def bet_result(db: Session, id: int):
    return db.query(models.Bet).filter(models.User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, name: str):
    db_user = models.User(name=name, balance = 100.0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_bet(db: Session, user_id: int, type: str, value: str, amount: float):
    db_bet = models.Bet(user_id=user_id, type=type, value=value, amount=amount)
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet

def create_table(db: Session):
    db_table = models.RouletteTable()
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


