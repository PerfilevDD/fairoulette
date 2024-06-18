import argparse, uvicorn
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from fairoulette import Randomizer, Bet, Table  # type: ignore

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from typing import Optional

import database.models as models
import database.database as database
import database.crud as crud
import database.schemas as schemas

import asyncio
import time
import threading

tables: list[Table] = []
results: list[int] = [0,0,0] # todo: auto size etc

app = FastAPI(
    title="Fairroulette"
)

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
@app.post("/users", response_model=schemas.User, tags=["User"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, name=user.name)


# get bet from user
@app.post("/bet", response_model=schemas.Bet, tags=["Bet"])
def create_bet(bet: schemas.BetBase, db: Session = Depends(get_db)):

    db_bet = crud.create_bet(db=db, user_id=bet.user_id, table_id=bet.table_id, type=bet.type, value=bet.value, amount=bet.amount)
    new_bet = Bet(bet.user_id, db_bet.id)
    
    print(bet)
    # bet's types
    if bet.type == 'number':
        new_bet.add_number_bet(int(bet.value), bet.amount)
    elif bet.type == 'col':
        # wir bekommen ein Array in str
        for digit in range(len(bet.value.split(",")) - 1):
            value = bet.value.split(",")[digit]
            new_bet.add_dozen_bet(int(value), bet.amount)
    elif bet.type == 'doz':
        # wir bekommen ein Array in str
        for digit in range(len(bet.value.split(",")) - 1):
            value = bet.value.split(",")[digit]
            new_bet.add_dozen_bet(int(value), bet.amount)
    elif bet.type == 'color':
        if 'red' == bet.value:
            new_bet.add_red_bet(bet.amount)
        else:
            new_bet.add_black_bet(bet.amount)
        
    tables[bet.table_id].add_or_update_bet_for_participant(bet.user_id, new_bet)
    
    user = crud.get_user_id(db, bet.user_id)
    user.balance -= bet.amount

    return crud.create_bet(db=db, user_id=bet.user_id, table_id=bet.table_id, type=bet.type, value=bet.value, amount=bet.amount)




@app.get("/users/{name}", response_model=schemas.User, tags=["User"])
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_name(db, name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# give a result to user
@app.get("/get_result/{user_id}/", response_model=schemas.Bet, tags=["Bet"])
def get_result(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_id(db, user_id)
    return user


#
@app.get("/get_result/{table_id}")
async def post_random(table_id: int):
    print(f'{results[table_id - 1]}')
    return {'result': results[table_id - 1]}

@app.get("/tables", tags=["Table"])
async def get_tables(db: Session = Depends(get_db)):

    return {
        "tables": [table.id for table in crud.get_tables(db)]
    }

@app.post("/table", tags=["Table"])
async def create_table(db: Session = Depends(get_db)):
    table = crud.create_table(db)
    return {
        "table": table.id
    }
@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse(url="/docs")


async def run_roulette_game():
    global result_random, results
    while True:
        await asyncio.sleep(5)
        for table in tables:
            result_random = table.calculate_result()
            results[table.get_table_id() - 1] = result_random
            print(f"Table: {table.get_table_id()} - Result: {result_random}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    for table in crud.get_tables(next(get_db())):
        tables.append(Table(table.id))
    asyncio.create_task(run_roulette_game())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-rd', '--round_duration', default=30)
    parser.add_argument('-p', '--port', type=int, default=8000, help="The port on which the api will be accessible.")
    parser.add_argument('-ho', '--host', default="localhost", help="The host on which the api will be accessible.")
    args = parser.parse_args()

    round_duration = args.round_duration
    uvicorn.run(app, host=args.host, port=args.port)
