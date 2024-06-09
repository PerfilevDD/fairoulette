from sqlalchemy.orm import Session

import database.models as models
import database.schemas as schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, name: str):
    db_user = models.User(name=name, balance = 0.0)
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


