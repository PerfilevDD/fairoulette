import requests

def get_random_number():
    url = "http://localhost:8000"
    response = requests.get(f"{url}/get_random_number")
    if response.ok:
        print(response.json())
        #print(response.json()['result'])

if __name__ == "__main__":
    while(True):
        result = get_random_number()