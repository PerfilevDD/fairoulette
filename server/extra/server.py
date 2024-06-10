from fastapi import FastAPI, Depends, HTTPException
from fairoulette import Randomizer, Bet, Table # type: ignore

from sqlalchemy.orm import  Session
import database.models as models
import database.database as database
import database.crud as crud
import database.schemas as schemas

import asyncio
import time
import threading
table = Table()


app = FastAPI()

# Database
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-data DONT DELETE, sonst macht ihr alles selbst noch mal!!!!111!

models.Base.metadata.create_all(bind=database.db)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, name=user.name)


# get bet from user
@app.post("/make_bet/", response_model=schemas.Bet)
def create_bet(bet: schemas.BetBase, db: Session = Depends(get_db)):
    print(bet)
    user = crud.get_user_id(db, bet.user_id)
    print(bet.user_id)
    new_bet = Bet(user.id)
    if bet.type == 'number':
       new_bet.add_number_bet(int(bet.value), bet.amount)
    table.add_or_update_bet_for_participant(bet.user_id, new_bet)
    return crud.create_bet(db=db, user_id=bet.user_id, type=bet.type, value=bet.value, amount=bet.amount)
    

@app.get("/users/{name}", response_model=schemas.User)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_name(db, name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# give a result to user
@app.get("/get_result/{user_id}/", response_model=schemas.Bet)
def get_result(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_id(db, user_id)
    return user

# 
@app.get("/get_result/")
async def post_random():
    print(f'{result_random}')
    return {'result': result_random}



async def run_roulette_game():
    global result_random
    while True:
        await asyncio.sleep(5)
        result_random = table.calculate_result()
        print(f"{result_random}")

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_roulette_game())