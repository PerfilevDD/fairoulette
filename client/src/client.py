import requests
url = "http://localhost:8000"

def get_random_number():
    response = requests.get(f"{url}/get_random_number")
    if response.ok:
        print(response.json())
        #print(response.json()['result'])
        
def register():
    name = "test3"
    try:
        r = requests.post(f"{url}/users/", json={'name': name})
        r.raise_for_status()
        print(r.json())
    except requests.exceptions.RequestException as e:
        pass
    
    
def make_bet():
    user_id = "2"
    type = "color"
    value = "black"
    amount = 10.0
    requests.post(f"{url}/make_bet/", json = {'user_id': user_id, "type": type, 'value': value, 'amount': amount})
    

if __name__ == "__main__":
    make_bet()
    #while(True):
        #result = get_random_number()