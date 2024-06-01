import requests

def get_random_number():
    url = "http://localhost:25565/get_random_number"
    #payload = {'x': x, 'y': y}
    #data = response.json()
    response = requests.post(url, json={"e":"e"})
    if response.ok:
        print(response.json())
    #data = response.json()
    #return data['result']

if __name__ == "__main__":
    while(True):
        #test_input = input()
        result = get_random_number()
        #print(f"Res: {result}")