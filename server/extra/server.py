from fastapi import FastAPI
from fairoulette import Randomizer # type: ignore
import time
import threading




import models, database

models.Base.metadata.create_all(bind=database.db)

app = FastAPI()

@app.get('/get_random_number')
async def get_random_number():
    randomizer = Randomizer()
    result = randomizer.get_random_number();
    print(f'{result}')
    return {'result': result}


from pydantic import BaseModel
class UserCreate(BaseModel):
    username: str

@app.post('/registration')
async def registration(user_data: UserCreate):
    username = user_data.username
    print(f'{username}')
    return {"username": username}

#def run_game():
    #while True:
        #time.sleep(30)
        #get_random_number(result)
        
#threading.Thread(target=run_game, daemon=True).start()