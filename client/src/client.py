import requests
url = "http://localhost:8000"

def get_random_number():
    response = requests.get(f"{url}/get_random_number")
    if response.ok:
        print(response.json())
        #print(response.json()['result'])
        
def registration():
    name = "test1"
    requests.post(f"{url}/registration", json = {'username': name})
    

if __name__ == "__main__":
    registration()
    #while(True):
        #result = get_random_number()