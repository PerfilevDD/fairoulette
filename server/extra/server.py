from fastapi import FastAPI
from fairoulette import Randomizer # type: ignore

app = FastAPI()

@app.get('/get_random_number')
async def get_random_number():
    randomizer = Randomizer()
    result = randomizer.get_random_number();
    print(f'{result}')
    return {'result': result}
