from fastapi import FastAPI, Depends, HTTPException
from fairoulette import Randomizer # type: ignore

from sqlalchemy.orm import  Session
import database.models as models
import database.database as database
import database.crud as crud
import database.schemas as schemas

import time
import threading


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
def create_bet(bet: schemas.BetCreate, db: Session = Depends(get_db)):
    return crud.create_bet(db=db, user_id=bet.user_id, type=bet.type, value=bet.value, amount=bet.amount)

'''
# give a result to user
@app.get("/result/{user_id}/", response_model=schemas.Bet)
def bet_result(user_id: int, balance, db: Session = Depends(get_db)):
    return crud.create_bet(db=db, user_id=bet.user_id, type=bet.type, value=bet.value, amount=bet.amount)

@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
'''

@app.get('/get_random_number')
async def get_random_number():
    randomizer = Randomizer()
    result = randomizer.get_random_number();
    print(f'{result}')
    return {'result': result}


#def run_game():
    #while True:
        #time.sleep(30)
        #get_random_number(result)
        
#threading.Thread(target=run_game, daemon=True).start()