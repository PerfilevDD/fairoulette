# LINK FOR CLIENT (with https etc.): 
# https://fairoulette.ctrl-felix.de

# LINK FOR GITHUB REPO:
# https://t.ly/QkICP
![image](https://github.com/PerfilevDD/fairoulette/assets/40623804/a28d46f7-bbaa-49de-bb69-ed155a8a0b70)


# Fairoulette

A fair copy of Game Roulette

## Contributors

- Daniil (CTO): GUI, Clint, Server
- Felix (CEO): Logic, Server

## Credits
- Sir Tim Berners-Lee: Thanks for the Internet
- Felix Boes: Dessen Vorlesungen die Grundlage für dieses Projekt bilden.

## Run client release
For Linux
```shell
chmod +x client_linux
./client_linux
```


## Setup for Server/Client
Install Requirements:
```shell

pip install -r requirements.txt
```
Compile cpp files
```shell
cd server &&
cmake -S . -B build/ &&
cmake --build build/ &&
cmake --install build
```

### Run Server
```shell
cd server/extra/
uvicorn server:app --reload
```

### Run Client
`python3 client/src/gui.py`




