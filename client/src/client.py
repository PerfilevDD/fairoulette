import requests

def calculate(x, y):
    url = "http://localhost:25565/calculate"
    payload = {'x': x, 'y': y}
    response = requests.post(url, json=payload)
    
    data = response.json()
    return data['result']

if __name__ == "__main__":
    while(True):
        x = 1
        y = 2
        result = calculate(x, y)
        print(f"Res: {result}")